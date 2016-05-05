# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function)

import json

from ansible import __version__ as ANSIBLE_VERSION

if ANSIBLE_VERSION.startswith('2'):
    from ansible.plugins.lookup import LookupBase
else:
    LookupBase = object

from trigger.tacacsrc import Tacacsrc

class LookupModule(LookupBase):
    '''
    Boilerplate Ansible LookupModule class.
    '''

    def __init__(self, basedir=None, **kwargs):
        self.basedir = basedir

    def run(self, terms, **kwargs):
        '''
        Normalize terms and args and perform lookup.

        Args:
          terms (str): Comma-delimited list of terms.
          terms (list): List of terms.

        '''
        ## Normalize terms to be a list
        if not isinstance(terms, list):
            terms = terms.split()
        realm = terms[0]
        tc = Tacacsrc()
        creds = dict(zip(('user', 'passwd', 'realm'), tc.creds[realm]))
        return [ json.dumps(creds) ]

