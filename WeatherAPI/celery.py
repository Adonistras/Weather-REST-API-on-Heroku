import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WeatherAPI.settings')
app = Celery('WeatherAPI')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'update_every_hour_weather': {
        'task': 'Update_weather',
        'schedule': crontab(minute=0, hour='*/1'),
    },
    'send_mail_every_evening': {
        'task': 'Send_mail',
        'schedule': crontab(minute=0, hour=21)
    }
}
