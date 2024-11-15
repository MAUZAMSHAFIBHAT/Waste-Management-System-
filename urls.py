"""
URL configuration for infosysproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from turtle import home
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from app.views import home_view  # Correct import from app views

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('signup/', include('app.urls')),
    path('', home_view, name='home'),  # This line adds the home view at the root URL
    path('', include('app.urls')),  # This includes your login URLs from the app


    # Password reset URLs
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]


if settings.DEBUG :
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_URL)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_URL)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)