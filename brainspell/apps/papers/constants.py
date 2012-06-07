# -*- coding: utf-8 -*-

from extended_choices import Choices

LABEL_TYPES = Choices(
    ('TASK',   'T', u"Task"),
    ('DOMAIN', 'D', u"Cognitive Domain"),
)

RATING_TYPES = Choices(
    ('LIKE',     1, u"Like"),
    ('DISLIKE', -1, u"Dislike"),
)

NEUROSYNTH_BASE_URL = 'http://neurosynth.org/studies/%d'

PUBMED_BASE_URL = 'http://www.ncbi.nlm.nih.gov/pubmed/%d'

PUBMED_DATE_FORMAT_LONG = '%Y %b %d'
PUBMED_DATE_FORMAT_NORMAL = '%Y %b'
PUBMED_DATE_FORMAT_SHORT = '%Y'

DOMAIN_NS_DC = '{http://purl.org/dc/terms/}'
DOMAIN_NS_OWL = '{http://www.w3.org/2002/07/owl#}'
DOMAIN_NS_RDF = '{http://www.w3.org/2000/01/rdf-schema#}'
DOMAIN_NS_SKOS = '{http://www.w3.org/2004/02/skos/core#}'

DEFAULT_SEARCH_LIMIT = 30

MAX_LABEL_LENGTH = 50

LABEL_FREE_INPUT_MARKER = 'other'