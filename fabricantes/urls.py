from django.urls import path
from . import views

app_name = "fabricantes"

urlpatterns = [
    path('lista/', views.listar, name='listar'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('excluir/<int:codigo>/', views.excluir, name='excluir'),
    path('editar/<int:codigo>/', views.editar, name='editar'),
]