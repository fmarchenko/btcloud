# -*- coding: utf-8 -*-
'''
Created on Jun 10, 2014

@author: Fedor Marchenko
'''

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext as _
from django.db.models.signals import post_save
from django.conf import settings
from btsync import settings as bt_settings
from btsync import btsync
import os

class BtUser(AbstractUser):
    folder = models.CharField(_('folder'), max_length=255, blank=True, null=True)
    secret = models.CharField(_('secret'), max_length=255, blank=True, null=True)
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
    
    def __unicode__(self):
        return self.username
        
IGNORE_ERRORS = (0, 104, 101)
        
def create_user_folder(sender, instance, **kwargs):
    if not instance.folder:
        folder_name = instance.username
        folder_path = os.path.join(settings.MEDIA_ROOT, 'btsync', folder_name)
        
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            
        instance.folder = folder_name
        
        add_result = btsync.add_folder(folder_path)
        
        if (add_result['error'] == 101):
            os.chown(folder_path, bt_settings.BTSYNC_SYSTEM_UID, bt_settings.BTSYNC_SYSTEM_GID)
        if not add_result['error'] in IGNORE_ERRORS:
            raise Exception('Error %s: %s' % (add_result['error'], add_result['message']))
        
        folders = btsync.get_folders()
        instance.secret = filter(
            lambda x: os.path.abspath(x['dir']) == os.path.abspath(folder_path), 
            folders
        )[0]['secret']
        instance.save()
             
post_save.connect(create_user_folder, BtUser)