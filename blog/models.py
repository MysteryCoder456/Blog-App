from django.db import models
from django.core.validators import MaxLengthValidator


class BlogList(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Blog(models.Model):
    blog_list = models.ForeignKey(BlogList, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    creationDate = models.DateTimeField()
    content = models.TextField(
        max_length=500,
        blank=True,
        validators=[MaxLengthValidator(500)]
    )
