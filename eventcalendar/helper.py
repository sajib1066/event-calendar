from django.contrib.sessions.models import Session
from django.utils import timezone
from django.contrib.auth.models import User


def get_current_user():
    active_sessions = Session.objects.filter(expire_date__gte=timezone.now())
    user_id_list = []
    for session in active_sessions:
        data = session.get_decoded()
        user_id_list.append(data.get("_auth_user_id", None))
    user = User.objects.get(id=user_id_list[0])
    return user
