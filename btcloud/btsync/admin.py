# -*- coding: utf-8 -*-
'''
Created on Jun 10, 2014

@author: Fedor Marchenko
'''

from django.contrib import admin
from btsync.models import BtUser
from django.contrib.auth.admin import UserAdmin as _UserAdmin
from django.utils.translation import ugettext, ugettext_lazy as _

class BtUserAdmin(_UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('BtSync info'), {'fields': ('folder', 'secret')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(BtUser, BtUserAdmin)