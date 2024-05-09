from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'), # URL para la vista de dashboard
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
]
