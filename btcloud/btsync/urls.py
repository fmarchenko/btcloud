# -*- coding: utf-8 -*-
'''
Created on Jun 10, 2014

@author: Fedor Marchenko
'''

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from btsync.views import CloudView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='btsync/frontpage.html'), name='frontpage_view'),
    url(r'^cloud/$', login_required(CloudView.as_view()), name='cloud_view'),
    url(r'^cloud/(?P<path>.*)/$', login_required(CloudView.as_view()), name='cloud_with_path_view'),
)