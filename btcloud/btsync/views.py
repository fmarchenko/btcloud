# -*- coding: utf-8 -*-
'''
Created on Jun 10, 2014

@author: Fedor Marchenko
'''

from django.views.generic import TemplateView
from django.http import HttpResponse
from django.conf import settings
from btsync import btsync
import json, os


get_full_path = lambda x, y: os.path.abspath(os.path.join(settings.MEDIA_ROOT, 'btsync', x, y))


class CloudView(TemplateView):
    template_name = 'btsync/cloud.html'
    
#     def get(self, request, *args, **kwargs):
#         if not kwargs.get('path', False):
#             return super(CloudView, self).get(request, *args, **kwargs)
# #         context = super(CloudView, self).get_context_data(**kwargs)
#         json_res = {}
#         user_secret = self.request.user.secret
#         full_path = get_full_path(self.request.user.folder, kwargs.get('path'))
#         all_files = btsync.get_files(secret=user_secret, path=kwargs.get('path'))
#          
#         print all_files
#          
#         return HttpResponse(json.dumps(json_res), mimetype="application/json")
    
    def get_context_data(self, **kwargs):
        context = super(CloudView, self).get_context_data(**kwargs)
        user_secret = self.request.user.secret
        all_files = btsync.get_files(secret=user_secret, path=kwargs.get('path', None))
        
        if kwargs.get('path'):
            dirs = kwargs.get('path').split('/')
            paths = []
            for i in range(len(dirs)):
                paths.append((dirs[i], '/'.join(dirs[:i+1])))
            context['paths'] = paths
        
        context['folder'] = btsync.get_folders(secret=user_secret)
        context['dirs'] = filter(lambda x: x['type'] == 'folder' and x['state'] != 'deleted', all_files)
        context['files'] = filter(lambda x: x['type'] == 'file' and x['state'] != 'deleted', all_files)
        
        return context