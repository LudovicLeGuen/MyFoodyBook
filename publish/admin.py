from django.contrib import admin
from .models import Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_field = ('recipe_steps', 'ingredients')
    search_fields = ['title', 'recipe_steps']
    list_display = (
        'title',
        'slug',
        'author',
        'created_on',
        'status'
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Class for the Comment section in the the admin panel.
    Organises the display of posts as well as filtering, search and other
    custom methods.
    """

    search_fields = ['recipe', 'name', 'body']
    list_filter = ('recipe', 'name', 'created_on', 'approved')
    list_display = ('name', 'email', 'recipe', 'created_on', 'approved')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)