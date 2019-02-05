from django.urls import path
from . import views

app_name='dojo'
urlpatterns = [
    path('new/', views.post_new),
    path('<int:pk>/edit/', views.post_edit),
    path('<int:x>', views.mysum),
    path('<name>/<age>/', views.hello),
    path('list1/', views.post_list1),
    path('list2/', views.post_list2),
  #  path('list3/', views.post_list3),
    path('excel/', views.excel_download),
]
