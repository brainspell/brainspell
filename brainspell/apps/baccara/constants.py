 # -*- coding: utf-8 -*-

from extended_choices import Choices

OPTIONAL = dict(blank=True, null=True)

GENDERS = Choices(
    ('FEMALE',      'F', u"Female"),
    ('MALE',        'M', u"Male"),
    ('OTHER',       'O', u"Other"),
    ('UNSPECIFIED', 'U', u"Unspecified"),
)

CONTENTS_MEDIA_POSITIONS = Choices(
    ('TOP',    'top',    u"Au-dessus du contenu"),
    ('LEFT',   'left',   u"A gauche du contenu"),
    ('RIGHT',  'right',  u"A droite du contenu"),
    ('BOTTOM', 'bottom', u"Sous le contenu"),
)

DEFAULT_MEDIA_POSITION = 'right'