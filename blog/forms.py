from django import forms
from django.utils import timezone
from .models import Blog, BlogList

list_choices = []
for ls in BlogList.objects.all():
    if ls.name != "Dev Logs":
        list_choices.append((ls.name, ls))


class NewBlogForm(forms.Form):
    blog_list = forms.CharField(label="Category", widget=forms.Select(choices=list_choices))
    title = forms.CharField(max_length=100, label="Title")
    author = forms.CharField(max_length=50, label="Author")

    creation_date = forms.DateField(
        label="Date (D/M/Y)",
        input_formats=["%d/%m/%Y"]
    )

    content = forms.CharField(label="Blog Content", max_length=500, widget=forms.Textarea)