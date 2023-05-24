# copied from Hana Belay
# https://dev.to/earthcomfy/creating-a-django-registration-login-app-part-ii-3k6
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import View
from .forms import RegisterForm
from django.views.generic import DetailView
from django.core.paginator import Paginator, EmptyPage
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from .forms import UpdateUserForm, UpdateProfileForm
from django.views.generic.list import ListView
from .models import Profile, User


# Registration view
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


class ShowUserProfile(DetailView):
    model = Profile
    template_name = 'users/user_profile.html'

    def get_context_data(self, *args, **kwarg):
        users = Profile.objects.all()        
        context = super(ShowUserProfile, self).get_context_data( *args, **kwarg)

        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        context["page_user"] = page_user
        return context

# Profile view
@login_required
def my_profile(request):
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
            return redirect(to='my-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(
        request,
        'users/profile.html',
        {'user_form': user_form, 'profile_form': profile_form}
        )


# Profile view
@login_required
def profile(request, user_id):
    if request.user.id == user_id:

        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    else:
        user = User.objects.get(id=user_id)
        user_form = UpdateUserForm(instance=user)
        profile_form = UpdateProfileForm(instance=user.profile)

    return render(request,'users/profile.html',
        {'user_form': user_form, 'profile_form': profile_form}
        )


# All users list
def show_all_users(request, page=1):
    data = Profile.objects.all()
    paginator = Paginator(data, 8)
    try:
        data = paginator.page(page)
    except EmptyPage:
        # if we exceed the page limit we return the last page
        data = paginator.page(paginator.num_pages)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'users/userslist.html', {"data": data})
