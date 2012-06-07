# -*- coding: utf-8 -*-

import logging

from django.db import models
from django.contrib.auth.models import User

from baccara.constants import OPTIONAL
from baccara.models import SuperModel

class Content(SuperModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    text = models.TextField(**OPTIONAL)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.title

class News(Content):
    class Meta:
        verbose_name_plural = u"News"


class Page(Content):
    pass
