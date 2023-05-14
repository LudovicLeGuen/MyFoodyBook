from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True, null=True)
    avatar = CloudinaryField('image', default='placeholder')
    bio = models.TextField()
    favorite_food = models.TextField()
    nationality = models.TextField()

    def __str__(self):
        return self.user.username


# Create profile when user signs in
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()


post_save.connect(create_profile, sender=User)
