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
