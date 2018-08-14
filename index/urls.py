from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index_views),
    url(r'^login/$', login_views, name='index_login'),
    url(r'^register/$', register_views, name='index_register'),
    url(r'^index/$', index_views),
]
