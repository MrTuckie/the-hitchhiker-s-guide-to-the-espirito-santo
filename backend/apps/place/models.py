from django.db import models

# As relações
# aaaaaaaaaaaaaa 
# caraca

class Place(models.Model):
    name = models.CharField(max_length=30)
    activity = None
    posts = None
