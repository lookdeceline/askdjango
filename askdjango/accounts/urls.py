from django.urls import path
from django.conf import settings
from django.contrib.auth import views as auth_views
from . import views

# app_name='accounts'

urlpatterns=[
    path('profile/', views.profile),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name= 'accounts/login_form.html'),
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page=settings.LOGIN_URL),
         name='logout'),
    path('profile/', views.profile, name='profile'),

]