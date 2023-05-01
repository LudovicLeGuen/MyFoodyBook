from .models import Comment, Recipe
from django import forms
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class RecipeForm(forms.ModelForm):
    """
    Recipe Form Class.
    Sets the model and fields for the recipe form.
    Also assigns summernote widget to certain form fields.
    """

    class Meta:

        model = Recipe

        # Summernote Widgets
        widgets = {
            'ingredients': SummernoteWidget(),
            'recipe_steps': SummernoteWidget(),
        }

        fields = (
            'title',
            'recipe_image',
            'preping_time',
            'cook_time',
            'serves',
            'excerpt',
            'ingredients',
            'recipe_steps',
            'status',
        )
