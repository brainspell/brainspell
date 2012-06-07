# -*- coding: utf-8 -*-

import logging
import datetime

from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse, Http404, QueryDict
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect

from papers.constants import LABEL_TYPES
from papers.models import Paper, Label

from constants import *

def homepage(request):

    papers = Paper.objects.order_by('?')[:NUM_PAPERS_ON_HOMEPAGE]
    labels = Label.objects.filter(type=LABEL_TYPES.DOMAIN, is_toplevel=True)

    context = {
        'papers': papers,
        'labels': labels,
    }
    return render_to_response('homepage.html',
        context, RequestContext(request))


