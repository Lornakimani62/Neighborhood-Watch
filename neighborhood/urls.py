from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$' ,views.index, name='index'),
    url(r'^accounts/profile/',views.profile, name='profile'),
    url(r'^business/',views.business,name='business'),
    url(r'^post_business/',views.post_business,name='post'),
    url(r'^contact/',views.contact,name='contact'),
    url(r'^notifications/', views.notify, name='notify'),
    url(r'^post_notify/', views.post_notify,name='post_notify'),
    url(r'^search/',views.search,name='search'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)