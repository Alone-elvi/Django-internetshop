from django.conf.urls import url, include
from django.contrib import admin
from auto_mngr import views

urlpatterns = [
    url(r'^auto_mngr/', views.auto_mngr, name='auto_mngr'),
]