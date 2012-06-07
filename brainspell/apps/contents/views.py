# -*- coding: utf-8 -*-

import logging
import datetime

from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse, Http404, QueryDict
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response, redirect

from baccara import ajax

from constants import *
from models import News, Page


def news(request):
    context = {
        'news': News.active.all()
    }
    return render_to_response('news.html',
        context, RequestContext(request))


def article(request, slug):
    context = {
        'article': get_object_or_404(News, slug=slug, is_active=True)
    }
    return render_to_response('article.html',
        context, RequestContext(request))


def page(request, slug):
    context = {
        'page': get_object_or_404(Page, slug=slug, is_active=True)
    }
    return render_to_response('page.html',
        context, RequestContext(request))
