from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# LABEL: REGISTER
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            usern = form.cleaned_data.get("username")
            messages.success(request, f"User {usern} has been registered succesfully!")
    else:
        form = UserCreationForm()

    return render(request, "user/register.html", {"form": form})
