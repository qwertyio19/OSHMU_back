from celery import shared_task
import time
from django.utils.timezone import now
from apps.students.models import SendingReport



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


@shared_task
def process_sending_report(report_id):
    time.sleep(1.5)  # ⏳ задержка 1.5 сек, снижает одновременную нагрузку

    report = SendingReport.objects.get(id=report_id)
    
    # здесь может быть отправка уведомления, логика проверки и т.п.
    print(f"Отчёт от студента {report.id} обработан")