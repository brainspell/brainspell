# -*- coding: utf-8 -*-

import logging

from constants import *
from models import Paper, Label


def search(query, return_objects=False):
    """ Basic search engine.

        Recognized search parameters:
        - a > (a)uthor      [contains]
        - id                [int]
        - j > (j)ournal     [contains]
        - l > (l)imit       [int]
        - p > (p)aper       [id]
        - q > (q)uery       [text]
        - t > (t)ag         [exact]

        If a (q)uery is passed, we should search for tags, journals,
        authors and papers containing this query and return 4 different
        result sets.

        Otherwise, we should search only for papers.

    """

    results = {
        'tags': [],
        'journals': [],
        'authors': [],
        'papers': [],
    }

    if query.get('q', None):
        
        param = query.get('q')
        logging.debug(param)

        tags = Label.objects.filter(name__icontains=param)
        limit = DEFAULT_SEARCH_LIMIT
        if query.get('l', None):
            limit = min(tags.count(), int(query.get('l')))
        tags = tags[:limit]
        results['tags'] = tags

        journals = list()
        j_papers = Paper.objects.filter(journal__icontains=param)
        for paper in j_papers:
            journals.append(paper.journal)
        results['journals'] = list(set(journals))

        authors = list()
        a_papers = Paper.objects.filter(authors__icontains=param)
        for paper in a_papers:
            p_authors = paper.authors.split(', ')
            for author in p_authors:
                if param.lower() in author.lower():
                    authors.append(author)
        results['authors'] = list(set(authors))

        papers = Paper.objects.filter(title__icontains=param)
        limit = DEFAULT_SEARCH_LIMIT
        if query.get('l', None):
            limit = min(papers.count(), int(query.get('l')))
        papers = papers[:limit]
        results['papers'] = papers

    else:

        # --- Targeted paper search

        papers = Paper.objects.all()

        if query.get('a', None):
            param = query.get('a')
            papers = papers.filter(authors__icontains=param)

        if query.get('id', None):
            param = query.get('id')
            papers = papers.filter(pk=param)

        if query.get('j', None):
            param = query.get('j')
            papers = papers.filter(journal__icontains=param)

        if query.get('t', None):
            param = query.get('t')
            papers = papers.filter(
                experiments__tags__label__name__icontains=param)

        papers = papers.distinct()

        limit = DEFAULT_SEARCH_LIMIT
        if query.get('l', None):
            limit = min(papers.count(), int(query.get('l')))

        papers = papers[:limit]
        if not return_objects:
            papers = [paper.as_json() for paper in papers]
            
        results['papers'] = papers

    logging.debug(u"search(): results: %s" % str(results))

    return results
