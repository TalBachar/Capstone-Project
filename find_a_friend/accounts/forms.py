from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        required=True,
        max_length=500
    )
    password = forms.CharField(
        label='Password',
        required=True,
        max_length=500,
        widget=forms.PasswordInput()
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None
        self.fields['username'].widget.attrs.update({'placeholder': 'Username'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Password'})


class SignupForm(UserCreationForm):
    password2 = forms.CharField(
        label="Confirm Password",
        strip=False,
        widget=forms.PasswordInput,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'placeholder': 'First Name'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Last Name'})
        self.fields['username'].widget.attrs.update({'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm password'})

    class Meta:
        model = User
        fields = ("username",
                  "first_name",
                  "last_name",
                  "email",
                  "password1",
                  "password2")


    def clean_email(self):
        email = self.cleaned_data['email']
        if not email:
            raise forms.ValidationError('Enter a valid email')
        return email

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update({'placeholder': 'Enter first name'})
        self.fields["last_name"].widget.attrs.update({'placeholder': 'Enter last name'})

    class Meta:
        model = User
        fields = ["first_name", "last_name"]
