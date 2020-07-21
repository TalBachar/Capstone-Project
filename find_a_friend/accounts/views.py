from django.contrib.auth import logout, authenticate, login
from django.contrib import messages, auth
from django.http import HttpResponseRedirect, Http404
from django.views.generic import CreateView, FormView, RedirectView
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from .forms import SignupForm, LoginForm

class SignupClass(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'accounts/form.html'
    success_url = '/login'

    extra_context = {
        'title': 'Find A Friend NYC'
    }

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(self.request, *args, **kwargs)

    def get_success_url(self):
        return self.success_url

    def post(self, request, *args, **kwargs):

        user_form = self.form_class(data=request.POST)

        if user_form.is_valid():
            user = user_form.save(commit=False)
            password = user_form.cleaned_data.get("password1")
            user.set_password(password)
            user.save()
            return redirect('accounts:login')
        else:
            return render(request, 'accounts/form.html', {'form': user_form})


class LoginClass(FormView):

    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('pets')

        context = {
            'form': LoginForm()
        }

        return render(request, 'accounts/login.html', context)

    def post(self, request, *args, **kwargs):
        context = self.authorize_or_get_error(request)

        if request.user.is_authenticated:
            return redirect('pets')
        else:
            return render(request, 'accounts/login.html', context)

    def authorize_or_get_error(self, request):
        data = {}

        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data

            user = authenticate(
                username=cd['username'],
                password=cd['password']
            )

            if user is not None:
                login(request, user)
                return data
            else:
                data['error'] = 'Username or Poassword is Incorrect!'
        else:
            data['error'] = 'User not registered'

        data['form'] = form
        return data

class LogoutClass(RedirectView):
    url = '/'

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return super(LogoutClass, self).get(request, *args, **kwargs)
