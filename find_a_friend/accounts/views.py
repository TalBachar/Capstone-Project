from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, RedirectView
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from .models import Pet
from .mailAlerts import sendMail
from .petfinderAPI import Query
from django.db import *
from .forms import SignupForm, UserUpdateForm, PetUpdateForm


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            #username = form.cleaned_data.get('username')
            return redirect('accounts:login')

    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})


@login_required
def profile_update(request):
    if request.method == 'POST':
        pet_form = PetUpdateForm(request.POST,
                                 request.FILES,
                                 instance=request.user.pet)
        if pet_form.is_valid():
            pet_form.save()
            sendMail.sendMail(request.user.first_name, request.user.email)
            return redirect('accounts:profile_update')

    else:
        pet_form = PetUpdateForm(instance=request.user.pet)

        # Query the DB, show results if exists
        logged_user_name = request.user.username
        logged_user_id = request.user.id
        user_pet = Pet.objects.get(user__username__contains=logged_user_name)

        # Get total results by user's criteria
        total_results = Query.get_total_results(
            user_pet.pet_type, user_pet.pet_age, user_pet.pet_breed)
        print("Total results: ", total_results)
        context = {
            'pet_form': pet_form,
            'user_criteria_type': user_pet.pet_type,
            'user_criteria_age': user_pet.pet_age,
            'user_criteria_breed': user_pet.pet_breed,
            'total_results': total_results,
        }

    return render(request, 'accounts/edit.html',  context)


class LogoutView(RedirectView):
    url = '/'

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        messages.success(request, 'You are logged out')
        return super(LogoutView, self).get(request, *args, **kwargs)


class ProfileHome(ListView):
    model = User
    template_name = "home.html"
    context_object_name = 'profile'

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)


class ProfileView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'accounts/myprofile.html'
    context_object_name = 'posts'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return User.objects.filter(username=user)
