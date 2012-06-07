# -*- coding:utf-8 -*-

import logging
import os

from lxml import etree

from django.conf import settings
from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify

from papers.constants import *
from papers.models import Label
import papers


class Command(BaseCommand):
    """ Import all domains from the XML extract provided by Russ Poldrack. """
    help = __doc__

    def handle(self, *args, **options):

        num_domains = num_imported_domains = 0

        domains_fn = os.path.join(settings.PROJECT_ROOT, 'data', 'domains.xml')

        tree = etree.parse(domains_fn)
        root = tree.getroot()

        for domain in root.findall('%sClass' % DOMAIN_NS_OWL):

            name_node = domain.find('%slabel' % DOMAIN_NS_RDF)
            cogat_id_node = domain.find('%sidentifier' % DOMAIN_NS_DC)
            def_node = domain.find('%sdefinition' % DOMAIN_NS_SKOS)
            top_node = domain.find('%shasTopConcept' % DOMAIN_NS_SKOS)
            if name_node is None or top_node is None:
                continue

            num_domains += 1

            name = name_node.text.strip().lower()
            logging.error('Importing concept: %s' % name)

            slug = slugify(name)
            type_ = LABEL_TYPES.DOMAIN

            definition = def_node.text if def_node is not None else ''
            cogat_id = cogat_id_node.text if cogat_id_node is not None else ''
            logging.error('  cognitive atlas ID: %s' % cogat_id)

            top_concept = top_node.text if top_node is not None else ''
            if top_concept:
                top_concept = top_concept.lower()
                logging.error('  Adding top concept: %s' % top_concept)
                try:
                    top_concept = Label.objects.get_or_create(
                        name=top_concept, type=type_, is_toplevel=True
                    )[0]
                except Exception, ex:
                    top_concept = Label.objects.filter(
                        name=top_concept, type=type_, is_toplevel=True
                    ).order_by('id')[0]
                logging.error('  Done.')
            else:
                top_concept = None

            new_label = Label.objects.create(
                name=name,
                slug=slug,
                type=type_,
                definition=definition,
                parent=top_concept,
                is_predefined=True,
                cognitive_atlas_id=cogat_id,
            )

            num_imported_domains += 1

        logging.error(u"Domains found: %d - Domains imported: %d" % (
            num_domains, num_imported_domains))
