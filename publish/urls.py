from . import views
from django.urls import path


urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path(
        'publish_recipe/',
        views.PublishRecipe.as_view(),
        name='publish_recipe'
        ),
    path('recipe/update/<int:pk>/', views.EditRecipe.as_view(),
         name='update_recipe'),
    path('my_foody_book/', views.MyFoodyBook.as_view(),
         name='my_foody_book'),
    path(
        'publish/<slug:slug>/',
        views.RecipeDetail.as_view(),
        name='recipe_details'
        ),

]
