from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("blogs/", views.blogs, name="new_blogs")
]