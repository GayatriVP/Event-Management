from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from EMSapp import views

urlpatterns = [url(r'book/', views.book_event, name='book_event'),
               url(r'^delete/(?P<part_id>[0-9]+)/$',
                   views.delete_event, name='delete_booking'),
               url(r'^edit/(?P<part_id>[0-9]+)/$', views.edit_event, name='edit_booking'), ]
