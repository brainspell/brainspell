# -*- coding:utf-8 -*-

import logging
import os

from lxml import etree

from django.conf import settings
from django.core.management.base import BaseCommand

from papers.constants import *
from papers.models import Paper, Experiment, Location


class Command(BaseCommand):
    """ Import all papers from the XML extract provided by Tal Yarkoni. """
    help = __doc__

    def handle(self, *args, **options):

        num_papers = num_imported_papers = 0
        num_experiments = num_imported_experiments = 0
        num_locations = num_imported_locations = 0

        papers_fn = os.path.join(settings.PROJECT_ROOT, 'data', 'papers.xml')

        parser = etree.XMLParser(recover=True)
        tree = etree.parse(papers_fn, parser=parser)
        root = tree.getroot()

        for paper in root.iterchildren():

            num_papers += 1

            # --- Parse basic data

            title = paper.find('title').text.strip()

            journal = paper.find('journal').text
            pubmed_id = paper.find('Medline_number').text
            doi = paper.find('doi').text

            authors = list()
            authors_node = paper.find('authors')
            for author_node in authors_node.iterchildren():
                authors.append(author_node.text.strip())
            authors = ', '.join(authors)

            # --- Parse PubMed data

            abstract = source = date_published = ''

            pubmed_node = paper.find('PubMed')
            try:
                abstract = pubmed_node.find('Abstract').text
            except:
                pass
            try:
                source = pubmed_node.find('Source').text
            except:
                pass
            try:    
                date_published = pubmed_node.find('DateOfPublication').text
            except:
                pass

            # --- Parse Neurosynth data

            neurosynth_node = paper.find('neurosynth')
            neurosynth_id = neurosynth_node.find('id').text.strip()
            neurosynth_space = neurosynth_node.find('space').text.strip()

            # --- Record Paper in the Django database

            try:
                new_paper = Paper.objects.create(
                    title=title.encode('utf-8'),
                    journal=journal.encode('utf-8'),
                    authors=authors.encode('utf-8'),
                    abstract=abstract.encode('utf-8'),
                    source=source.encode('utf-8'),
                    date_published=date_published,
                    doi=doi,
                    pubmed_id=pubmed_id,
                    neurosynth_id=neurosynth_id,
                    neurosynth_space=neurosynth_space
                )
                num_imported_papers += 1
            except Exception, ex:
                logging.error(u"Cannot save paper '%s': %s" % (title, ex))
                continue

            # --- Parse experiments

            experiments_nodes = paper.findall('experiment')
            for experiment_node in experiments_nodes:

                num_experiments += 1

                # --- Record Experiment in the Django database

                title = experiment_node.find('title').text.strip()
                try:
                    new_experiment = Experiment.objects.create(
                        title=title,
                        paper=new_paper
                    )
                    num_imported_experiments += 1
                except Exception, ex:
                    logging.error(
                        u"Cannot save experiment '%s': %s" % (title, ex))
                    continue

                # --- Parse locations

                locations_nodes = experiment_node.findall('location')
                for location_node in locations_nodes:

                    num_locations += 1

                    location_raw = location_node.text.strip()
                    x, y, z = [int(s) for s in location_raw.split(',')]

                    try:
                        new_location = Location.objects.create(
                            x=x, y=y, z=z,
                            experiment=new_experiment
                        )
                        num_imported_locations += 1
                    except Exception, ex:
                        logging.error(
                            u"Cannot save location for '%s': %s" % (
                                new_experiment.title, ex))
                        continue

        logging.error(u"Papers found: %d - Papers imported: %d" % (
            num_papers, num_imported_papers))
        logging.error(u"Experiments found: %d - Experiments imported: %d" % (
            num_experiments, num_imported_experiments))
        logging.error(u"Locations found: %d - Locations imported: %d" % (
            num_locations, num_imported_locations))
