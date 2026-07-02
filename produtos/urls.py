from django.urls import path
from . import views 

app_name = "produtos"

urlpatterns = [
    path('lista/', views.listar, name='listar'),
    path('cadastro/', views.cadastro, name='cadastro'),
]