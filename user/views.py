from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# LABEL: REGISTER
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            usern = form.cleaned_data.get("username")
            print(f"User {usern} has been registered!")
        else:
            print("uhhh")
    else:
        form = UserCreationForm()

    return render(request, "user/register.html", {"form": form})
