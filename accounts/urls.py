from django.urls import path
from .views import UserRegisterView, UserLoginView, LogoutView, UserProfileView,UserProfileUpdateView ,home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView, name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile/update/', UserProfileUpdateView.as_view(), name='profile_update'),
]