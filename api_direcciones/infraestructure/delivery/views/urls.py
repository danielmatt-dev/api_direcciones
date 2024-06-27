from django.urls import path

from api_direcciones.infraestructure.delivery.views.direccion_views import DireccionView


direccion_path = 'direcciones'

urlpatterns = [
    path(f'{direccion_path}/<int:codigo_postal>/', DireccionView.as_view(), name='direccion_detail')
]
