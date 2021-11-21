from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from EMSapp import views

urlpatterns = [url(r'book/', views.book_event, name='book_event')]
