from . import views
from django.contrib import admin
from django.urls import path

# 404
handler404 = views.page_404

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path("admin/", admin.site.urls),
    path('publish_recipe/', views.PublishRecipe.as_view(),
         name='publish_recipe'),
    path('collect/<slug:slug>', views.RecipeCollect.as_view(),
         name='recipe_collect'),
    path('recipe/update/<int:pk>/', views.EditRecipe.as_view(),
         name='update_recipe'),
    path('my_foody_book/', views.MyFoodyBook.as_view(),
         name='my_foody_book'),
    path('recipe/remove/<int:pk>/', views.DeleteRecipe.as_view(),
         name='delete_recipe'),
    path('publish/<slug:slug>/', views.RecipeDetail.as_view(),
         name='recipe_details'
         ),
]
