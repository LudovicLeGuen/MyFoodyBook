# copied from Hana Belay
# https://dev.to/earthcomfy/creating-a-django-registration-login-app-part-ii-3k6
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .forms import RegisterForm
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from .forms import UpdateUserForm, UpdateProfileForm
from django.views.generic.list import ListView
from .models import Profile


class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'users/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(
                request,
                f'Congratulations {username}! Your account is created.'
                )

            return redirect(to='/')

        return render(request, self.template_name, {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
            )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(
        request,
        'users/profile.html',
        {'user_form': user_form, 'profile_form': profile_form}
        )



class UserListView(ListView):

    model = Profile
    template_name = 'users/userslist.html'