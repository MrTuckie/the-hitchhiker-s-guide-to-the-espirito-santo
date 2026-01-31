from django.db import models

# As relações
# A place must have zero or n activities
# An activity must have a place
# caraca


class Place(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"Place - {self.name}"
