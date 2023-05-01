from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Publishing Status
STATUS = ((0, "Draft"), (1, "Published"))


class Recipe(models.Model):
    """
    Recipe model class.

    """

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipe_posts"
        )
    recipe_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField()
    preping_time = models.PositiveIntegerField()
    cook_time = models.PositiveIntegerField()
    serves = models.PositiveIntegerField()
    ingredients = models.TextField()
    recipe_steps = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name="recipe_likes", blank=True
        )

    # Order of recipes on screen: Newest first
    class Meta:
        ordering = ['-created_on']

    # Title String Function
    def __str__(self):
        return self.title

    # Likes count Function
    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    """
    Comment model class.

    """
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="comments"
        )
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    # Order of comments on screen: Oldest first
    class Meta:
        ordering = ['created_on']

    # Title String Function
    def __str__(self):
        return f"Comment {self.body} by {self.name}"
