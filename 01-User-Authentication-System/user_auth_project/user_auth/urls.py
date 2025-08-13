from django.urls import path
from .views import CustomLoginView, RegisterPage, LoggedInView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', RegisterPage.as_view(), name='register'),
    path('logged-in/', LoggedInView.as_view(), name='logged_in'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', CustomLoginView.as_view(), name="login"), #base url
]