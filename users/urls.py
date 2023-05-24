from users import views
from django.urls import path
from .views import profile, RegisterView, my_profile, ShowUserProfile


urlpatterns = [
    path('', views.my_profile, name='my-profile'),
    path('profile/<int:user_id>', views.profile, name='users-profile'),
    path('show_profile/<int:pk>', ShowUserProfile.as_view(), name='show-profile'),
    path('userslist/', views.show_all_users, name='users-list'),    
    path('register/', RegisterView.as_view(), name='users-register'),

]
