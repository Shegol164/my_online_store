from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .forms import CustomAuthenticationForm

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html',
        form_class=CustomAuthenticationForm
    ), name='login'),
]