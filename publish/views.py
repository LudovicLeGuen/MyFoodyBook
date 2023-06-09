from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Recipe
from django.views.generic.edit import DeleteView
from .forms import CommentForm, RecipeForm
from django.views.generic import TemplateView
from django.template.defaultfilters import slugify
from django.contrib import messages
from django.urls import reverse_lazy


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class RecipeDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipe_details.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by(
            "-created_on"
            )
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
            messages.success(request, 'Your comment is not awaiting approval')
        else:
            comment_form = CommentForm()

        return render(
            request,
            "recipe_details.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class MyFoodyBook(generic.ListView):
    """
    Returns recipe objects created and collected by the logged in user.
    """

    model = Recipe
    template_name = 'my_foody_book.html'
    paginate_by = 6

    def get(self, request, *args, **kwargs):

        user = request.user
        queryset_dict = {
            }
        if user.is_authenticated:
            queryset = Recipe.objects.filter(
                author=request.user.id).order_by(
                '-created_on').filter(
                        status=1) | Recipe.objects.filter(likes=user).filter(
                        status=1).order_by('-created_on')
            queryset_dict = {
                'my_foody_book': queryset
            }

        return render(
            request,
            self.template_name,
            queryset_dict
        )


class PublishRecipe(View):
    """
    Used to post a recipe by a logged in user.
    Combined with the RecipeForm and the publish_recipe template.

    """

    form_class = RecipeForm
    initial = {'key': 'value'}
    template_name = 'publish_recipe.html'

    def get(self, request, *args, **kwargs):

        form = self.form_class(initial=self.initial)
        return render(
            request,
            self.template_name,
            {
                'form': form,
                'posted': False,
            }
        )

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            form.instance.author = request.user
            form.instance.slug = slugify(form.instance.title)
            recipe = form.save(commit=False)
            recipe.save()
            return render(
                request,
                'publish_recipe.html',
                {
                    'posted': True,
                }
            )
        else:
            return render(
                request,
                'publish_recipe.html',
                {
                    'form': form,
                    'failed': True,
                    'posted': False,
                }
            )


class EditRecipe(TemplateView):
    """
    Used to edit a recipe by the user.
    Combined with the form and the update_recipe template.
    """

    model = Recipe
    template_name = 'update_recipe.html'

    def get(self, request, pk, *args, **kwargs):
        """
        Get method to render template and form.
        """

        recipe = Recipe.objects.get(pk=pk)
        form = RecipeForm(instance=recipe)

        return render(
            request,
            self.template_name,
            {
                'form': form,
                'posted': False
            }
        )

    def post(self, request, pk, *args, **kwargs):

        recipe = Recipe.objects.get(pk=pk)
        form = RecipeForm(request.POST, request.FILES, instance=recipe)

        if form.is_valid():
            form.save()
            form.instance.slug = slugify(form.instance.title)
            recipe = form.save(commit=False)
            recipe.save()

            return render(
                request,
                self.template_name,
                {
                    'form': form,
                    'posted': True
                }
            )
        else:
            return render(
                request,
                self.template_name,
                {
                    'form': form,
                    'failed': True,
                    'posted': False,
                }
            )


# Class inspired by www.tutorialspoint.com :
# https://www.tutorialspoint.com/adding-a-deleteview-in-django#:~:text=DeleteView%20is%20a%20view%20in,helpful%20in%20real%2Dworld%20projects.
class DeleteRecipe(DeleteView):
    model = Recipe
    template_name = 'delete_recipe.html'
    success_url = reverse_lazy("my_foody_book")


class RecipeCollect(View):

    def post(self, request, slug):
        """
        Post method for Collecting and removing a recipe
        """

        recipe = get_object_or_404(Recipe, slug=slug)

        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe_details', args=[slug]))


# 404 Taken from
# https://levelup.gitconnected.com/django-customize-404-error-page-72c6b6277317
def page_404(request, exception):
    return render(request, "404.html")
