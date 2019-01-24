# blogs/urls.py
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list),
    path('<int:id>', views.post_detail),
]