# -*- coding:utf-8 -*-

import os
import csv
import string
import logging

from django.conf import settings
from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify

from papers.constants import *
from papers.models import Label


class Command(BaseCommand):
    """ Import all tasks from the CSV extract provided by Roberto Toro. """
    help = __doc__

    def handle(self, *args, **options):

        num_tasks = num_imported_tasks = 0

        tasks_fn = os.path.join(settings.PROJECT_ROOT, 'data', 'tasks.csv')

        reader = csv.reader(open(tasks_fn, 'rb'), delimiter=';', quotechar='"')
        for row in reader:

            cogat_id = row[0]
            name = string.capwords(row[1])
            logging.error('Importing task: %s (%s)' % (name, cogat_id))

            slug = slugify(name)
            type_ = LABEL_TYPES.TASK
            num_tasks += 1

            new_label = Label.objects.create(
                name=name,
                slug=slug,
                type=type_,
                is_predefined=True,
                cognitive_atlas_id=cogat_id,
            )

            num_imported_tasks += 1

        logging.error(u"Tasks found: %d - Tasks imported: %d" % (
            num_tasks, num_imported_tasks))
