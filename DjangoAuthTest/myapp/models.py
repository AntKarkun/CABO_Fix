from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

# Create your models
class Сomplaint(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #user = models.ForeignKey(User.username, on_delete=models.CASCADE)

    fixer = models.TextField()
    room = models.TextField()
    problema = models.TextField()
    resheno = models.BooleanField(default=False)
    reshaetsa = models.BooleanField(default=False)
    namee = models.TextField()
