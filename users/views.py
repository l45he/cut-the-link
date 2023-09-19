from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, AddLinkForm
from django.contrib.auth.decorators import login_required
from .models import URLs

# Create your views here.


def links(request):
    links = URLs.objects.filter(username=request.user)
    post = request.POST

    if request.method == "POST":
        addLink = AddLinkForm(post)
        if addLink.is_valid():
            instance = addLink.save(commit=False)
            instance.username = request.user
            instance.save()
            return redirect('links')
    else:
        addLink = AddLinkForm()



    return render(request, 'users/links.html',
                      {'addLink': addLink, 'links': links, 'post': post})

class RegisterPage(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('home')
    template_name = "users/registration.html"


@login_required
def profile(request):
    if request.method == 'POST':
        updateUserForm = UserUpdateForm(request.POST, instance=request.user)

        if updateUserForm.is_valid():
            updateUserForm.save()
            return redirect('home')

    else:
        updateUserForm = UserUpdateForm(instance=request.user)

    data = {
        'updateUserForm': updateUserForm,
    }

    return render(
        request,
        'users/profile.html',
        data
    )