from . import views
from django.urls import path


urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path(
        'publish_recipe/',
        views.PublishRecipe.as_view(),
        name='publish_recipe'
        ),
    path('collect/<slug:slug>', views.RecipeCollect.as_view(), name='recipe_collect'),
    path('recipe/update/<int:pk>/', views.EditRecipe.as_view(),
         name='update_recipe'),
    path('my_foody_book/', views.MyFoodyBook.as_view(),
         name='my_foody_book'),
    path('recipe/remove/<int:pk>/', views.RemoveRecipe.as_view(),
         name='remove_recipe'),
    path(
        'publish/<slug:slug>/',
        views.RecipeDetail.as_view(),
        name='recipe_details'
        ),

]
