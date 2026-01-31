from django.db import models
from ..place.models import Place


class Post(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    description = models.TextField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post - {str(self.description[0:10])}"
