# -*- coding: utf-8 -*-
'''
Created on Jun 10, 2014

@author: Fedor Marchenko
'''

from btsyncapi import BtSyncApi
import settings

btsync = BtSyncApi(settings.BTSYNC_HOST, settings.BTSYNC_PORT, settings.BTSYNC_LOGIN, settings.BTSYNC_PASSWORD)