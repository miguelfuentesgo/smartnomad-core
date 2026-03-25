# apps/authentication/urls.py
from django.urls import path, include

urlpatterns = [
    # Rutas de Login, Logout, User, etc.
    path('', include('dj_rest_auth.urls')),
    
    # Ruta de Registro
    path('registration/', include('dj_rest_auth.registration.urls')),
]