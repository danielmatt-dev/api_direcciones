"""
URL configuration for api_direcciones project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api_direcciones.infraestructure.config.direccion_view_factories import post_crear_usuario_factory

api_path = 'api'

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f'{api_path}/register/', post_crear_usuario_factory, name='crear_usuario'),
    path(f'{api_path}/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(f'{api_path}/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path(f'{api_path}/', include('api_direcciones.infraestructure.delivery.views.urls'))
]
