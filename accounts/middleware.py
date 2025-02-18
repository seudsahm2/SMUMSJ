# accounts/middleware.py
from django.shortcuts import redirect
from django.urls import reverse


class RoleAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.user.is_authenticated:
            if request.path.startswith('/amir/') and not request.user.is_amir():
                return redirect(reverse('member-dashboard'))
            elif request.path.startswith('/member/') and request.user.role == 'GUEST':
                return redirect(reverse('guest-home'))
