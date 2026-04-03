from django.db import models
from apps.authentication.models import Profile

class Place(models.Model):
    """
    Represents a destination or point of interest in smartnomad.
    """

    name = models.CharField(max_length=255)
    
    # visit_time could be an Integer (minutes) or a CharField (e.g., "2-3 hours").
    visit_time = models.CharField(max_length=100)
    
    # avg_price stores the estimated cost of visiting this place.
    avg_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    # TextField allows for long descriptions without a character limit.
    description = models.TextField()
    
    # Storing the location of the place to compare it with the Profile's location.
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='places',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name