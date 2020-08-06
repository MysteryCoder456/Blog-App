from django.db import models
from django.core.validators import MaxLengthValidator
from django.utils import timezone
from vote.models import VoteModel


class BlogList(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Blog(VoteModel, models.Model):
    blog_list = models.ForeignKey(BlogList, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=150)
    creation_date = models.DateField()
    content = models.TextField(
        max_length=500,
        blank=True,
        validators=[MaxLengthValidator(500)]
    )

    def __str__(self):
        return f"Title: {self.title}, id: {self.id}, Points: {self.votes.count()}"


class Comment(models.Model):
    blog_post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    author = models.CharField(max_length=150)
    creation_date = models.DateField()
    content = models.TextField(
        max_length=200,
        blank=True,
        validators=[MaxLengthValidator(200)]
    )

    def __str__(self):
        return f"Parent Post: {self.blog_post.title}, Content: {self.content}, id: {self.id}"
