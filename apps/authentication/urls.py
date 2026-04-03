# apps/authentication/urls.py
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Rutas de Login, Logout, User, etc.
    path('', include('dj_rest_auth.urls')),

    # Endpoints JWT explicitos bajo la misma estructura /api/auth/.
    path('jwt/create/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Ruta de Registro
    path('registration/', include('dj_rest_auth.registration.urls')),
]
