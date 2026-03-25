# This code defines serializers for converting user and profile model instances
# into JSON representations for use in a REST API (using Django REST Framework).

from rest_framework import serializers
from django.contrib.auth.models import User
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import Profile


class EmailRegisterSerializer(RegisterSerializer):
    username = None

    def get_cleaned_data(self):
        return {
            'email': self.validated_data.get('email', ''),
            'password1': self.validated_data.get('password1', ''),
        }

# Serializer for the Profile model
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile                        # This serializer maps to the Profile model
        fields = ['photo', 'last_lat', 'last_lng']  # Only include photo, last_lat, and last_lng fields in API output

# Serializer for the User model, also includes the related profile info
class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)   # Adds a 'profile' field to the user output, using ProfileSerializer

    class Meta:
        model = User                            # This serializer maps to the built-in User model
        fields = ['id', 'username', 'email', 'first_name', 'profile']  # Outputs these fields, including the nested profile

# In summary:
# - ProfileSerializer serializes custom user profile data (like photo, latitude, longitude).
# - UserSerializer serializes basic user info and nests a readonly profile field.
# - These serializers are useful to create clean and structured JSON responses for user/account APIs.