from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    followings = models.ManyToManyField("self", related_name = "followers", symmetrical=False)
    image = models.ImageField(upload_to="profile_img/", null=True, blank=True)
    info = models.TextField(null=True, blank=True)
