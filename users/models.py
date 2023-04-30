from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = CloudinaryField('image', default='placeholder')
    bio = models.TextField()
    favorite_food = models.TextField()
    nationality = models.TextField()


    def __str__(self):
        return self.user.username
