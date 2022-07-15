from django.urls import path
from . import views
urlpatterns = [
    path('',views.login,name="login"),
    path("home.html", views.home, name="home"),
]
