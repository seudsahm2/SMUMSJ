# accounts/forms.py
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin  # Add this import
from django.views.generic import UpdateView  # Add this import
from allauth.account.forms import SignupForm as AllAuthSignupForm  # Rename import
from django.urls import reverse_lazy  # Add this import
from .models import CustomUser
User = get_user_model()


class CustomSignupForm(AllAuthSignupForm):  # Use renamed import
    phone = forms.CharField(max_length=20, required=True)

    def save(self, request):
        user = super().save(request)
        user.phone = self.cleaned_data['phone']
        user.save()
        return user


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
