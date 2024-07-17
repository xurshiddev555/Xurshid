from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.forms import ModelForm, ImageField
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from apps.forms import ProfileFormView
from apps.models import AbstractUser


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'username', 'email', 'password')

    def clean_password(self):
        password = self.cleaned_data.get('password')
        return make_password(password)


class ProfileFormView(FormView):
    form_class = ProfileFormView
    template_name = 'apps/profile.html'

    def form_valid(self, form):
        data = form.save(commit=False)
        print(data)

    def form_invalid(self, form):
        data = form.errors
        print(data)


class RegisterFormView(FormView):
    template_name = 'apps/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return redirect('login')
