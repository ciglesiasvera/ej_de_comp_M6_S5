from django.urls import path
from .views import verificar_palindromo

urlpatterns = [
    path('verificar/<str:palabra>/', verificar_palindromo, name='verificar_palindromo'),
]
