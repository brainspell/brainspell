# -*- coding: utf-8 -*-

import json
import logging

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core import serializers

from baccara.constants import OPTIONAL

from constants import *


class ExportablePaperManager(models.Manager):
    def export(self):
        pass


class Paper(models.Model):
    title = models.TextField()
    journal = models.CharField(max_length=255, **OPTIONAL)
    authors = models.TextField(**OPTIONAL)
    abstract = models.TextField(**OPTIONAL)
    source = models.TextField(**OPTIONAL)
    date_published = models.CharField(max_length=255, **OPTIONAL)

    doi = models.CharField(max_length=255, **OPTIONAL)
    pubmed_id = models.IntegerField(**OPTIONAL)
    neurosynth_id = models.IntegerField(**OPTIONAL)
    neurosynth_space = models.CharField(max_length=32, **OPTIONAL)

    objects = ExportablePaperManager()

    class Meta:
        pass

    def __unicode__(self):
        return self.title if self.title else u"<ID:%d>" % self.id

    def get_absolute_url(self):
        return "%spaper/%s" % (settings.PROJECT_URL, self.id)

    @property
    def authors_as_list(self):
        return self.authors.split(', ')

    @property
    def year_published(self):
        return self.date_published.split(' ')[0]

    @property
    def pubmed_url(self):
        return PUBMED_BASE_URL % self.pubmed_id

    @property
    def neurosynth_url(self):
        return NEUROSYNTH_BASE_URL % self.neurosynth_id

    def as_json(self):
        json_data = serializers.serialize('json', [self], fields=(
            'title', 'journal', 'authors', 'date_published'))
        json_data = json.loads(json_data)
        json_data = json_data[0].get('fields')
        json_data[u'id'] = self.id
        return json_data

    def as_xml(self):
        return serializers.serialize('xml', [self])


class Experiment(models.Model):
    title = models.TextField()
    paper = models.ForeignKey('Paper', related_name='experiments')

    class Meta:
        pass
        
    def __unicode__(self):
        return self.title if self.title else u"<ID:%d>" % self.id

    def tasks(self):
        return self.tags.filter(label__type=LABEL_TYPES.TASK)

    def main_tasks(self):
        return self.tasks().filter(level=1)

    def level1_tasks(self):
        return self.main_tasks()

    def domains(self):
        return self.tags.filter(label__type=LABEL_TYPES.DOMAIN)

    def main_domains(self):
        return self.domains().filter(level=1)

    def level1_domains(self):
        return self.main_domains()

    def _tag(self, user, label_id, label_name, label_type, parent_id=None):

        logging.debug(u"_tag(): label_id: %s" % label_id)
        logging.debug(u"_tag(): label_name: %s" % label_name)
        logging.debug(u"_tag(): label_type: %s" % label_type)
        logging.debug(u"_tag(): parent_id: %s" % parent_id)

        # --- Get or create matching Label
        parent_tag = Tag.objects.get(pk=parent_id) if parent_id else None
        parent_label = parent_tag.label if parent_id else None
        logging.debug(u"_tag(): parent_label: %s" % parent_label)

        # --- Get or create Label
        if label_id == LABEL_FREE_INPUT_MARKER:
            label = Label.objects.create(
                name=label_name.lower(), type=label_type, parent=parent_label)
        else:
            label = Label.objects.get(pk=int(label_id))

        # --- Get or create matching Tag
        level = parent_tag.level + 1 if parent_id else 1
        tag, is_new_tag = Tag.objects.get_or_create(
            label=label, experiment=self, level=level)

        if is_new_tag:
            try:
                tag.parent = parent_tag if parent_tag else None
                tag.save()
            except Exception, ex:
                logging.error(u"_tag(): %s" % ex)

            try:
                tag.created_by = user if user else None
                tag.save()
            except Exception, ex:
                logging.error(u"_tag(): %s" % ex)

        # --- Record Tag Instance
        ti = TagInstance.objects.create(tag=tag)
        try:
            ti.user = user
            ti.save()
        except Exception, ex:
            pass

        return tag.id

    def add_task(self, user, task_id, task_name, parent_id=None):
        return self._tag(
            user, task_id, task_name, LABEL_TYPES.TASK, parent_id)

    def add_domain(self, user, domain_id, domain_name, parent_id=None):
        return self._tag(
            user, domain_id, domain_name, LABEL_TYPES.DOMAIN, parent_id)

    @property
    def community_name(self):

        # --- TODO

        return 'X vs. Y'

    @property
    def community_domains(self):

        # --- TODO

        return list()


class Location(models.Model):
    experiment = models.ForeignKey('Experiment', related_name='locations')
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()

    class Meta:
        pass
        
    def __unicode__(self):
        return u"(%f, %f, %f)" % (self.x, self.y, self.z)


class Label(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200)
    type = models.CharField(max_length=1, choices=LABEL_TYPES.CHOICES)
    parent = models.ForeignKey('self', **OPTIONAL)
    definition = models.TextField(**OPTIONAL) 
    cognitive_atlas_id = models.CharField(max_length=32, **OPTIONAL)
    is_toplevel = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

    @property
    def is_predefined(self):
        return self.cognitive_atlas_id is not None

    @property
    def option_name(self):
        opt_name = self.name
        if len(opt_name) > MAX_LABEL_LENGTH:
            opt_name = opt_name[:MAX_LABEL_LENGTH] + '...'
        return opt_name.title()

    @staticmethod
    def get_tasks():
        """ Return a list of {name, value} dicts for available tasks. """

        lst = list()
        labels = Label.objects.filter(type=LABEL_TYPES.TASK)
        for label in labels:
            lst.append({
                'name': (label.name[:MAX_LABEL_LENGTH] + '...' \
                    if len(label.name) > MAX_LABEL_LENGTH      \
                        else label.name).title(),
                'value': label.id
            })
        return lst
        
    @staticmethod
    def get_domains(parent=None, level=0):                                       # --- FIXME: I can haz cache? :)
        """ Return a list of {name, value} dicts for available domains. """

        lst = list()

        if not parent:
            domains = Label.objects.filter(is_toplevel=True)
        else:
            domains = Label.objects.filter(parent=parent)

        for domain in domains:
            lst.append({
                'name': ' %s %s' % (
                    '-' * level * 2,
                    domain.option_name,
                ),
                'value': domain.id,
            })
            lst.extend(
                Label.get_domains(domain, level+1)
            )

        return lst


class Tag(models.Model):
    label = models.ForeignKey('Label')
    experiment = models.ForeignKey('Experiment', related_name='tags')
    created_by = models.ForeignKey('auth.User', **OPTIONAL)
    level = models.IntegerField(default=0)
    parent = models.ForeignKey('self', **OPTIONAL)
    num_likes = models.IntegerField(default=0)
    num_dislikes = models.IntegerField(default=0)

    class Meta:
        pass
        
    def __unicode__(self):
        return u"%s/%s" % (self.label, self.experiment)

    @property
    def as_json(self):
        return serializers.serialize('json', [self])

    @property
    def name(self):
        return self.label.name

    @property
    def is_predefined(self):
        return self.label.is_predefined

    @property
    def cognitive_atlas_id(self):
        return self.label.cognitive_atlas_id

    @property
    def score(self):
        return self.num_likes - self.num_dislikes

    @property
    def sub_tags(self):
        return Tag.objects.filter(
            label__parent=self.label).order_by('label__name')

    @property
    def contrast_tasks(self):
        return Tag.objects.filter(
            parent=self, label__type=LABEL_TYPES.TASK
        ).order_by('label__name')


    def update_counters(self):

        # --- Count Ratings
        num_likes = num_dislikes = 0
        ratings = Rating.objects.filter(tag=self)
        for rating in ratings:
            if rating.type == RATING_TYPES.LIKE:
                num_likes +=1
            else:
                num_dislikes += 1

        # --- Record updated counters
        self.num_likes = num_likes
        self.num_dislikes = num_dislikes
        self.save()

    def _rate(self, user, rating_type):
        rating, is_new = Rating.objects.get_or_create(
            tag=self, user=user, type=rating_type)
        if is_new:
            self.update_counters()
        return is_new

    def like(self, user):
        return self._rate(user, RATING_TYPES.LIKE)

    def dislike(self, user):
        return self._rate(user, RATING_TYPES.DISLIKE)

class TagInstance(models.Model):
    tag = models.ForeignKey('Tag')
    user = models.ForeignKey('auth.User', **OPTIONAL)

    class Meta:
        pass
        
    def __unicode__(self):
        return u"%s/%s" % (self.tag, self.user.username)


class Rating(models.Model):
    tag = models.ForeignKey('Tag')
    user = models.ForeignKey('auth.User')
    type = models.IntegerField(choices=RATING_TYPES.CHOICES)

    class Meta:
        pass
        
    def __unicode__(self):
        return u"Rating #%d" % self.id
