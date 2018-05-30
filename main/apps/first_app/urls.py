from django.conf.urls import url
from . import views           
urlpatterns = [
    url(r'^$', views.dashboard), 
    url(r'^registerprocess$', views.register_process), 
    url(r'^loginprocess$', views.login_process), 
    url(r'^login$', views.login), 
    url(r'^register$', views.register), 
]

