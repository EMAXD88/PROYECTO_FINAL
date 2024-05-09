from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('upload/', views.upload, name='upload'),
    path('listarData/', views.listarData, name='listarData'),
    path('borrar/<int:registro_id>/', views.borrar_registro, name='borrar_registro'),
]
