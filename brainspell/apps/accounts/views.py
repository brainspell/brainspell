# -*- coding: utf-8 -*-

import logging
import datetime

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, QueryDict
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.views.decorators.http import require_POST

from baccara import ajax

from models import Profile
from forms import ProfileForm


@require_POST
def register(request):

    query = request.POST
    email = query.get('email', None)
    password = query.get('password', None)

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        user = User.objects.create_user(email, email, password)
        profile = Profile.objects.create(user=user, email=email)

    user = authenticate(username=email, password=password)    
    if user is not None:
        do_login(request, user)

    return redirect(query.get('next', '/'))


# def login(request):
#     context = {
#
#     }
#     return render_to_response('login.html',
#         context, RequestContext(request))


@login_required
def logout(request):
    do_logout(request)
    return redirect(request.GET.get('next', '/'))


def forgot(request):
    context = {

    }
    return render_to_response('forgot.html',
        context, RequestContext(request))


def forgot_ok(request):
    context = {

    }
    return render_to_response('forgot_ok.html',
        context, RequestContext(request))


@login_required
def profile(request):
    profile = Profile.objects.get_or_create(
        user=request.user, email=request.user.email)
    if profile[1]:
        profile[0].save()
    profile = profile[0]

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        form = ProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
    }
    return render_to_response('profile.html',
        context, RequestContext(request))
