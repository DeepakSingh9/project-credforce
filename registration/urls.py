from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
             url(r'^home',views.dashboard,name='home'),
             url(r'^follow/(?P<pk>\d+)/$',views.follow,name='follow'),
             url(r'account/(?P<pk>\d+)/$',views.account,name='account'),
             url(r'login/$',views.user_login,name='login'),
             url(r'registration/$',views.user_registration,name='registration'),
             url(r'logout/$',views.user_logout,name='logout'),
             url(r'^upload/$',views.profile_image_upload,name='imageupload'),
             url(r'account/(?P<pk>\d+)/$', views.account, name='account'),

             ]