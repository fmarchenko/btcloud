# -*- coding: utf-8 -*-
'''
Created on Jun 10, 2014

@author: Fedor Marchenko
'''

from django import template
from btsync.btsyncapi import BtSyncApi

register = template.Library()

@register.filter
def fix_decode(value):
    return BtSyncApi.fix_decode(value)