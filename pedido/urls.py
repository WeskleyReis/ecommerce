from django.urls import path, include
from . import views


app_name = 'pedido'

urlpatterns = [
    path('pagar/', views.Pagar.as_view(), name='pagar'),
    path('fechamento/', views.Fechamento.as_view(), name='fechamento'),
    path('detalhe/<int:pk>/', views.Detalhe.as_view(), name='detalhe'),
]