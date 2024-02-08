from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, UpdateUserForm, UpdateProfileForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.conf import settings
from .models import Profile


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            current_user = form.save(commit=False)

            form.save()

            send_mail('Welcome to My Planner', 'Congratulation on creating your account', settings.DEFAULT_FROM_EMAIL, [current_user.email])

            profile = Profile.objects.create(user=current_user)

            messages.success(request, 'Your account was created')

            return redirect('login')

    context = {'form': form}
    return render(request, 'account/register.html', context)


def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(authenticate, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                return redirect('profile')

    context = {'form': form}
    return render(request, 'account/login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('home')


@login_required(login_url='login')
def profile(request):

    profile_pic = Profile.objects.get(user=request.user)


    context = {'profile_pic': profile_pic}
    return render(request, 'account/profile.html', context)


@login_required(login_url='login')
def profile_management(request ):
    form = UpdateUserForm(instance=request.user)

    profile = Profile.objects.get(user=request.user)

    form2 = UpdateProfileForm()

    if request.method == 'POST':

        form = UpdateUserForm(request.POST, instance=request.user)

        form2 = UpdateProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            form.save()

            return redirect('profile')

        if form2.is_valid():
            form2.save()

            return redirect('profile')

    context = {'UserUpdateForm': form, 'ProfileUpdateForm': form2}
    return render(request, 'account/profile_management.html', context)


@login_required(login_url='login')
def delete_account(request):

    if request.method == 'POST':

        deleteUser = User.objects.get(username=request.user)

        deleteUser.delete()

        return redirect('home')

    return render(request, 'account/delete_account.html')
