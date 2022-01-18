from django.contrib import auth
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.forms import ShopUserLoginForm, ShopUserCreationForm, ShopUserChangeForm, ShopUserProfileEditForm


def login(request):
    redirect_to = request.GET.get('next', '')

    if request.method == 'POST':
        form = ShopUserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            redirect_to = request.POST.get('redirect-to')
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return HttpResponseRedirect(redirect_to or reverse('main:index'))
    else:
        form = ShopUserLoginForm()

    context = {
        'page_title': 'логин',
        'form': form,
        'redirect_to': redirect_to,
    }
    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))


def register(request):
    if request.method == 'POST':
        form = ShopUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        form = ShopUserCreationForm()

    context = {
        'page_title': 'регистрация',
        'form': form,
    }
    return render(request, 'authapp/register.html', context)


@transaction.atomic
def edit(request):
    if request.method == 'POST':
        form = ShopUserChangeForm(request.POST, request.FILES,
                                  instance=request.user)
        profile_form = ShopUserProfileEditForm(request.POST,
                                               instance=request.user.profile)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.is_valid()
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = ShopUserChangeForm(instance=request.user)
        profile_form = ShopUserProfileEditForm(instance=request.user.profile)

    context = {
        'page_title': 'редактирование',
        'form': form,
        'profile_form': profile_form
    }
    return render(request, 'authapp/update.html', context)
