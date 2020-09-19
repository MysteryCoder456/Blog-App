from django import forms
from django.utils import timezone
from .models import Blog, BlogList

list_choices = []
for ls in BlogList.objects.all():
    if ls.name != "Dev Logs":
        list_choices.append((ls.name, ls))


class BlogSortForm(forms.Form):
    category = forms.CharField(label="Category", widget=forms.Select(choices=list_choices), required=False)


class NewBlogForm(forms.Form):
    blog_list = forms.CharField(label="Category", widget=forms.Select(choices=list_choices))
    title = forms.CharField(max_length=100, label="Title")
    content = forms.CharField(label="Blog Content", max_length=500, widget=forms.Textarea)


class NewCommentForm(forms.Form):
    content = forms.CharField(max_length=200)
