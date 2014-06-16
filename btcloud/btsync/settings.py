# -*- coding: utf-8 -*-
'''
Created on Jun 10, 2014

@author: Fedor Marchenko
'''

from django.conf import settings

BTSYNC_LOGIN = getattr(settings, 'BTSYNC_LOGIN', None)
BTSYNC_PASSWORD = getattr(settings, 'BTSYNC_PASSWORD', None)
BTSYNC_HOST = getattr(settings, 'BTSYNC_HOST', '127.0.0.1') 
BTSYNC_PORT = getattr(settings, 'BTSYNC_PORT', '8888')
BTSYNC_API_KEY = getattr(settings, 'BTSYNC_API_KEY', None)
BTSYNC_SYSTEM_UID = getattr(settings, 'BTSYNC_SYSTEM_UID', None)
BTSYNC_SYSTEM_GID = getattr(settings, 'BTSYNC_SYSTEM_GID', None)