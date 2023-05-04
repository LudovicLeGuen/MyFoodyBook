from users import views
from django.urls import path
from .views import profile, RegisterView
from users.views import UserListView


urlpatterns = [
    path('', views.profile, name='users-profile'),
    path('userslist/', UserListView.as_view(), name='users-list'),
    path('register/', RegisterView.as_view(), name='users-register'),
]
