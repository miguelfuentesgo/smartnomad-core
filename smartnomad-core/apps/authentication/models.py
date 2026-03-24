from django.db import models

# Create your models here.
Profile = models.Model(
    user = models.OneToOneField(User, on_delete=models.CASCADE),
    photo = models.ImageField(upload_to='profile_photos/'),
    last_lat = models.FloatField(),
    last_lng = models.FloatField(),
)