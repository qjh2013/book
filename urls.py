from django.conf.urls.defaults import *
from library.views import start,create,search,dele,updat,result

urlpatterns = patterns('',
    (r'^start/$', start),
    (r'^create/$',create),
    (r'^update/$',updat), 
	(r'^delete',dele),
	(r'^result/$',result),
	(r'^search/$',search),
)
