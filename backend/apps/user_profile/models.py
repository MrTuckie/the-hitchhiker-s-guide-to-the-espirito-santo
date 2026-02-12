from django.contrib.auth.models import User
from django.db import models

from apps.place.models import Place


class UserProfile(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=False, default=None, null=True
    )
    place = models.ForeignKey(
        Place, on_delete=models.DO_NOTHING, blank=False, default=None, null=True
    )

    def __str__(self):
        return f"UserProfile de {self.user.username}"
