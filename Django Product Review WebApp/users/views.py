# Import necessary modules
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse_lazy


# Define the register view method
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created, {username}! Now you can log in.')
            return redirect('login')
        else:
            messages.warning(request, 'Unable to create an account. Please correct the errors.')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form, 'title': 'JK Product Reviews - Register'})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')  # Replace 'home' with the name of your home view
        else:
            messages.warning(request, 'Error updating your profile. Please correct the errors.')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {'u_form': u_form, 'p_form': p_form, 'title': 'Profile'}
    return render(request, 'users/profile.html', context)

class ChangePasswordView(PasswordChangeView):
    template_name = 'users/change_password.html'  # Create this template
    success_url = reverse_lazy('change-password-done')  # Name of the URL pattern for password change done

class PasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'users/change_password_done.html'  # Create this template