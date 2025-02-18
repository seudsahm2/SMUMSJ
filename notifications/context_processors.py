# notifications/context_processors.py
from .models import Notification


def user_notifications(request):
    if request.user.is_authenticated:
        return {'notifications': Notification.objects.filter(user=request.user, is_read=False)[:5]}
    return {'notifications': []}
