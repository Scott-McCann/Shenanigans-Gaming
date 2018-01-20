from django.conf.urls import url
from . import views

app_name = 'tsgonline'

urlpatterns = [
    url(r'^$', views.view_index, name='index' ),
    url(r'^createaccount/$', views.new_user, name='create-account',)
]
