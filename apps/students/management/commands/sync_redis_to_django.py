from django.core.management.base import BaseCommand
from students.models import StudentProfile, Document, DiaryEntry
import redis
from django.conf import settings
import json

redis_client = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB,
    password=settings.REDIS_PASSWORD  # если есть
)
class Command(BaseCommand):
    help = 'Импорт данных из Redis в Django SQLite'

    def handle(self, *args, **options):
        r = redis.Redis(host='localhost', port=6379, db=0)
        
        student_keys = r.keys('student:*')
        for key in student_keys:
            data = r.hgetall(key)
            StudentProfile.objects.update_or_create(
                full_name=data.get(b'full_name').decode(),
                defaults={
                    'phone_number': data.get(b'phone_number', b'').decode(),
                    'institution': data.get(b'institution', b'').decode()
                }
            )
            self.stdout.write(f"Обновлён студент: {data.get(b'full_name').decode()}")

        self.stdout.write("Синхронизация завершена!")