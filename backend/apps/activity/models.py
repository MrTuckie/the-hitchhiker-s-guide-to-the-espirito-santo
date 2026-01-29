from django.db import models
from ..place.models import Place


class Activity(models.Model):
    class Meta:
        verbose_name = "Activity"
        verbose_name_plural = "Activities"

    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    description = models.TextField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)
