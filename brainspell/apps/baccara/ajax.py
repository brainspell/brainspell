#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
    import json
except ImportError:
    import simplejson as json

OBJECT_STATUS_TRUE = 1
OBJECT_STATUS_FALSE = 0

ACTION_STATUS_OK = 1
ACTION_STATUS_FAIL = 0

class Feedback:

    VALID_FEEDBACK_ATTRIBUTES = (
        'object_status', 'action_status', 'message', 'message_id', 'raw_data')

    def __init__(self, **kwargs):
        [setattr(self, key, value)                                           \
            for key,value in kwargs.iteritems()                               \
                if key in self.VALID_FEEDBACK_ATTRIBUTES] 

    def as_dict(self):
        return dict((key,value)                                              \
            for key,value in self.__dict__.iteritems()                        \
                if key in self.VALID_FEEDBACK_ATTRIBUTES)

    @property
    def as_json(self):
        return json.dumps(self.as_dict())

