from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.Login, name="login"),
    path('signup/', views.SignUp, name="signup"),
    path('home/', views.Home, name="home"),
    path('signout/', views.SignOut, name="signout"),
    path('new_post/', views.NewPost, name="new_post"),
]
