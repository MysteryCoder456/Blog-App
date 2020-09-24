from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("blogs/", views.blogs, name="new_blogs"),
    path("blog/<int:blog_id>", views.blog_detail, name="blog_detail"),
    path("createblog/", views.create_blog, name="create_blog"),
    path("dev/", views.dev_logs, name="dev_logs"),
    path("categories/", views.categories, name="categories"),
]
