from django.conf.urls import url
from basic_app import views

#TEMPLATE TAGGING
app_name = 'basic_app'
# django will automatically look for this variable and set this equal to name of the application.
# THIS WILL ALLOW US TO USE TEMPLATE TAGGING TO ACTUALLY TELL DJANGO, LOOK INTO 'BASIC_APP' AND THEN FIND 
# THE URL THAT MATCHES

urlpatterns = [
	url(r'^relative/$', views.relative, name = 'relative'),
	url(r'^other/$', views.other, name = 'other'),
]