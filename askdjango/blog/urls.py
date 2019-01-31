# blogs/urls.py
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('detail/<int:id>', views.post_detail, name ='post_detail'),
]