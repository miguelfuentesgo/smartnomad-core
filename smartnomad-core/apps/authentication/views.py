from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth.models import User

class CustomLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        # Intentamos buscar al usuario por email primero
        email = request.data.get('email')
        password = request.data.get('password')
        
        try:
            user_obj = User.objects.get(email=email)
            username = user_obj.username
        except User.DoesNotExist:
            return Response({"error": "Credenciales inválidas"}, status=400)

        # Usamos la lógica estándar de DRF con el username encontrado
        serializer = self.serializer_class(data={'username': username, 'password': password},
                                           context={'request': request})
        serializer.is_is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        
        return Response({
            'token': token.key,
            'user': UserSerializer(user).data
        })