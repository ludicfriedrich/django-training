"""
URL configuration for merchex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.welcome, name='welcome'),
    path('accounts/login/', views.login_user, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logout_user, name="logout"),
    
    path('bands/', views.band_list, name='band_list'),
    path('bands/<int:id>/', views.band_detail, name='band_detail'),
    path('bands/add/', views.band_create, name='band_create'),
    path('bands/<int:id>/update/', views.band_update, name='band_update'),
    path('bands/<int:id>/delete/', views.band_delete, name='band_delete'),
    
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('email-sent', views.email_sent, name='email_sent'),
    
    path('listings/', views.listings, name='listing_list'),
    path('listings/<int:id>/', views.listing_detail, name='listing_detail'),
    path('listing/add/', views.listing_create, name='listing_create'),
    path('listings/<int:id>/update/', views.listing_update, name='listing_update'),
    path('listing/<int:id>/delete/', views.listing_delete, name='listing_delete')
]
