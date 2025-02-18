from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django import forms
from .models import CustomUser
from .forms import CustomSignupForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class SignUpView(CreateView):
    model = CustomUser
    form_class = CustomSignupForm
    template_name = 'accounts/signup.html'
    success_url = '/accounts/login/'


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'


class CustomLogoutView(LogoutView):
    next_page = '/'

# accounts/forms.py


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'phone']

# accounts/views.py


class ProfileView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = ProfileUpdateForm
    template_name = 'accounts/profile.html'
    success_url = reverse_lazy('member-dashboard')

    def get_object(self):
        return self.request.user
