# copied from Hana Belay https://dev.to/earthcomfy/creating-a-django-registration-login-app-part-ii-3k6
from django.shortcuts import render, redirect 
from django.contrib import messages
from django.views import View
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required


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
            messages.success(request, f'Welcome to the Foody Book {username}! Your account is created.')

            return redirect(to='/')

        return render(request, self.template_name, {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')
