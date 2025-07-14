from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Указываем настройки Django по умолчанию
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.base')

app = Celery('core')

# Загружает конфигурацию из Django settings, префикс CELERY_
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически находит задачи из всех зарегистрированных приложений
app.autodiscover_tasks()