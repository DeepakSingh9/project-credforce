from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^post/(?P<pk>\d+)/(?P<slug>[\w-]+)/$',views.post_detail,name='post_detail'),
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/new/$',views.post_new,name='post_new'),
    url(r'^profile/(?P<pk>\d+)/$',views.profile,name='profile'),
    url(r'^post/(?P<pk>\d+)/(?P<slug>[\w-]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^comment/(?P<pk>\d+)/$',views.comment,name='comment'),
    url(r'^smallpost/$',views.small_post,name='smallpost'),
    url(r'^about_us/$',views.about_us,name='about_us'),
    url(r'^privacy_policy/$',views.privacy_policy,name='privacy_policy'),
    url(r'^terms/$',views.terms_and_conditions,name='terms'),
    url(r'^blog_published/(?P<pk>\d+)/$',views.blog_published,name='blog_published'),
]