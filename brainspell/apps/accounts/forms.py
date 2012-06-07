# -*- coding: utf-8 -*-

import logging

from django import forms
from django.forms import ModelForm, ValidationError
from django.conf import settings
from django.contrib.auth.models import User

from models import Profile


class ProfileForm(ModelForm):
    password = forms.CharField(required=False, widget=forms.PasswordInput)

    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    class Meta:
        model = Profile

    def save(self, force_insert=False, force_update=False):

        profile = super(ProfileForm, self).save()

        user = profile.user
        dirty = False

        if self.cleaned_data['email']:
            user.username = user.email = self.cleaned_data['email']
            dirty = True

        if self.cleaned_data['password']:
            user.set_password(self.cleaned_data['password'])
            dirty = True
                    
        if self.cleaned_data['first_name']:
            user.first_name = self.cleaned_data['first_name']
            dirty = True

        if self.cleaned_data['last_name']:
            user.last_name = self.cleaned_data['last_name']
            dirty = True

        if dirty:
            user.save()

        return profile
