# -*- coding: utf-8 -*-

import json
import logging
import datetime

from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse, Http404, QueryDict
from django.template import Template, Context, RequestContext
from django.template.loader import render_to_string
from django.shortcuts import render_to_response, redirect
from django.views.decorators.csrf import csrf_exempt

from baccara import ajax

from models import Paper, Experiment, Tag, Label
from search import search as do_search

def paper(request, id):
    try:
        paper = Paper.objects.get(pk=int(id))
    except Paper.DoesNotExist:
        raise Http404

    # --- New tag?
    if request.method == 'POST':
        query = request.POST

        experiment_id = query.get('experiment_id')
        try:
            experiment = Experiment.objects.get(pk=experiment_id, paper=paper)
        except Exception, ex:
            logging.error(u"paper(): Cannot fetch Experiment: %s" % ex)
            raise Http404
            
        action = query.get('action')
        if action.endswith('task'):
            action_method = experiment.add_task
        if action.endswith('domain'):
            action_method = experiment.add_domain

        tag_id = action_method(
            request.user,
            query.get('label'),
            query.get('label_free', None),
            query.get('parent_id', None))

        return redirect('%s#tag-%s' % (request.path, tag_id))

    tasks = Label.get_tasks()
    domains = Label.get_domains()

    # logging.debug(u"Tasks: %s" % str(tasks))
    # logging.debug(u"Domains: %s" % str(tasks))

    context = {
        'paper': paper,
        'tasks': tasks,
        'domains': domains,
    }
    return render_to_response('paper.html',
        context, RequestContext(request))


def search(request):
    query = request.GET
    results = do_search(query)
    context = {
        'query': query.get('q'),
        'results': results,
    }
    return render_to_response('search.html',
        context, RequestContext(request))


def export(request):
    """ Export should simply be like search, only with XML results. """
    query = request.GET
    results = do_search(query, return_objects=True)

    context = {
        'papers': results['papers'],
    }
    rendered = render_to_string('export.xml', context)

    response = HttpResponse(rendered, mimetype='text/xml') 
    # response['Content-Disposition'] = 'attachment; filename="brainspell.xml"'
    return response


# -----------------------------------------------------------------------------

AJAX_VALID_ACTIONS  = ('like', 'dislike', 'autocomplete')
AJAX_POST_ACTIONS   = ('like', 'dislike')
AJAX_LOGGED_ACTIONS = ('like', 'dislike')

@csrf_exempt
def ajax_do(request, action):
    
    if not action in AJAX_VALID_ACTIONS:
        raise Http404

    if action in AJAX_LOGGED_ACTIONS and not request.user.is_authenticated():
        raise Http404

    action_status = ajax.ACTION_STATUS_FAIL
    object_status = ajax.OBJECT_STATUS_FALSE
    raw_data = None
    message  = None

    user = request.user

    query = request.GET
    if action in AJAX_POST_ACTIONS:
        query = request.POST

    object_id = query.get('id', None)

    try:

        # --- Action: Like/dislike
        if action.endswith('like'):

            tag = Tag.objects.get(pk=object_id)

            if action.startswith('dis'):
                action_method = tag.dislike
            else:
                action_method = tag.like

            rating_was_added = action_method(user)

            action_status = rating_was_added
            object_status = ajax.OBJECT_STATUS_TRUE
            raw_data = json.loads(tag.as_json)

        # --- Action: Autocomplete
        elif action == 'autocomplete':

            q = query.get('query')          # --- (q)uery
            t = query.get('type')           # --- (t)ype: [T|D]
            p = int(query.get('parent'))    # --- (p)arent id

            labels = Label.objects.filter(
                name__istartswith=q,
                type=t,
            )
            if p > 0:
                labels = labels.filter(
                    parent=Label.objects.get(pk=p))

            quoted_labels = list()
            for label in labels:
                quoted_labels.append("'%s'" % label.name)
            quoted_labels = list(set(quoted_labels))

            response = "{query:'%s', suggestions:[%s]}" % (
                q, ', '.join(quoted_labels))
            return HttpResponse(response)


    except Exception, ex:
        logging.error(u"ajax(%s): ERROR: %s" % (action, ex))

    # --- Build & return ajax feedback
    feedback = ajax.Feedback(
        action_status=action_status,
        object_status=object_status,
        raw_data=raw_data,
        message=message,
    )
    return HttpResponse(feedback.as_json)

