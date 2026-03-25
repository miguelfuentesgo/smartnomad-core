from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    last_lat = models.FloatField(blank=True, null=True)
    last_lng = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.user.username