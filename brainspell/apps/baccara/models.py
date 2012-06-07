# -*- coding: utf-8 -*-

import logging

from django.db import models
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.models import User


class ActiveManager(models.Manager):
    def get_query_set(self):
        return super(ActiveManager, self).get_query_set().filter(is_active=True)

class SuperModel(models.Model):
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('auth.User', blank=True, null=True,
        related_name="%(app_label)s_%(class)s_author")

    objects = models.Manager()
    active = ActiveManager()

    class Meta:
        abstract = True
        ordering = ['-date_created']

class SuperModelAdmin(admin.ModelAdmin):

    readonly_fields = ('created_by', 'date_created',)

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'created_by', None) is None:
            obj.created_by = request.user
        obj.save()
