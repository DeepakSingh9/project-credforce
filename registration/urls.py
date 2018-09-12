from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
             url(r'^home',views.dashboard,name='home'),
             url(r'^follow/(?P<pk>\d+)/$',views.follow,name='follow'),
             url(r'^unfollow/(?P<pk>\d+)/$',views.unfollow,name='unfollow'),
             url(r'account/(?P<pk>\d+)/$',views.account,name='account'),
             url(r'login/$',views.user_login,name='login'),
             url(r'registration/$',views.user_registration,name='registration'),
             url(r'logout/$',views.user_logout,name='logout'),
             url(r'upload/$',views.profile_image_upload,name='imageupload'),
             url(r'account/(?P<pk>\d+)/$', views.account, name='account'),
             url(r'password_reset/$',auth_views.password_reset,{'template_name': 'registration/PasswordFiles/password_reset_form.html'},name='password_reset'),
             url(r'password_reset_done/$',auth_views.password_reset_done,{'template_name':'registration/PasswordFiles/password_reset_done.html'},name='password_reset_done'),
             url(r'password_reset_confirm/$',auth_views.password_reset_confirm,{'template_name':'registraion/PasswordFiles/password_reset_confirm.html'},name='password_reset_confirm'),
             url(r'reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth_views.password_reset_confirm,{'template_name':'registration/PasswordFiles/password_reset_done.html'},name='password_reset_confirm'),
             url(r'reset/done/$',auth_views.password_reset_complete,name='password_reset_complete'),
              ]


