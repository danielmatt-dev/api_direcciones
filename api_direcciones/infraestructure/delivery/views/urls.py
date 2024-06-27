from django.urls import path

from api_direcciones.infraestructure.config.direccion_view_factories import get_direcciones_factory

direccion_path = 'direcciones'

urlpatterns = [
    path(f'{direccion_path}/<int:codigo_postal>/', get_direcciones_factory, name='direccion_view')
]
