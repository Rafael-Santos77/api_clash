"""
URL configuration for wiki project.

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
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from clash.api import viewsets
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



route = routers.DefaultRouter()

route.register(r'heroina', viewsets.HeroinaViewset, basename= 'heroina')
route.register(r'king', viewsets.KingViewset, basename= 'king')
route.register(r'quenn', viewsets.QuennViewset, basename= 'quenn')
route.register(r'warden', viewsets.WardenViewset, basename= 'warden')
route.register(r'avatarheroes', viewsets.AvatarheroesViewset, basename= 'avatar')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('heroes/', include(route.urls)),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
