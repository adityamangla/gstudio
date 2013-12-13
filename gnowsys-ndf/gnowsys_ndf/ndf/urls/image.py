from django.conf.urls import patterns, url

from django.views.generic import TemplateView

from gnowsys_ndf.ndf.views import *



urlpatterns = patterns('gnowsys_ndf.ndf.views.imageDashboard',
                        url(r'^(?P<image_id>[\w-]+)$', 'imageDashboard', name='image'),
                        #url(r'^images/', 'imageDashboard', name='imageDashboard'),                                                 
                        url(r'^imageThumbnail/(?P<_id>[\w-]+)$', 'getImageThumbnail', name='getImageThumbnail'),
                        url(r'^fullImage/(?P<_id>[\w-]+)$', 'getFullImage', name='getFullImage'),
                        url(r'^image_search/$', 'image_search', name='image_search'),
)
