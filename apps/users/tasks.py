from celery import shared_task
import time
from django.utils.timezone import now



@shared_task
def log_user_login(user_id, ip_address):
    from apps.users.models import User
    from apps.users.models import LoginLog

    user = User.objects.get(id=user_id)
    LoginLog.objects.create(
        user=user,
        full_name=user.get_full_name() or user.username,
        ip_address=ip_address,
        role=user.role
    )