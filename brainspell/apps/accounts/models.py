# -*- coding: utf-8 -*-

import logging

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

from baccara.constants import OPTIONAL

from constants import *


class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    email = models.CharField(max_length=255)
    about = models.TextField(**OPTIONAL)