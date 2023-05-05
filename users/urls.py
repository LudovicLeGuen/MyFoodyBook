from users import views
from django.urls import path
from .views import profile, RegisterView


urlpatterns = [
    path('', views.profile, name='users-profile'),
    path('userslist/', views.show_all_users, name='users-list'),
    path('register/', RegisterView.as_view(), name='users-register'),
]
