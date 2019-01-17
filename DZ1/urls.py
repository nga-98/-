from django.conf.urls import url
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^picture_list', views.picture_list, name='picture_list'),
    url(r'^picture/(?P<pk>\d+)/$', views.picture_detail, name='picture_detail'),
    url(r'^picture/new/$', views.picture_new, name='picture_new'),
    url(r'^picture/(?P<pk>\d+)/edit/$', views.picture_edit, name='picture_edit'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)