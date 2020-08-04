from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth


from .forms import SignupForm, UserUpdateForm, PetUpdateForm



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('accounts:login')

    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})


@login_required
def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        pet_form = PetUpdateForm(request.POST,
                                         request.FILES,
                                         instance=request.user.pet)
        if user_form.is_valid() and pet_form.is_valid():
            user_form.save()
            pet_form.save()
            return redirect('accounts:profile_update')

    else:
        user_form = UserUpdateForm(instance=request.user)
        pet_form = PetUpdateForm(instance=request.user.pet)

    context = {
        'user_form': user_form,
        'pet_form': pet_form
    }
    return render(request, 'accounts/edit.html', context)

class ProfileHome(ListView):
    model = User
    template_name =  "home.html"
    context_object_name = 'profile'

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

class ProfileView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'accounts/myprofile.html'
    context_object_name ='posts'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return User.objects.filter(username=user)
