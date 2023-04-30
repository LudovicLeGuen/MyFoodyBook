from . import views
from django.urls import path


urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path(
        'publish/<slug:slug>/',
        views.RecipeDetail.as_view(),
        name='recipe_details'
        ),

]
