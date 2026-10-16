import os
from celery import Celery

# 1. Point Celery to our Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# 2. Instantiate the Celery app
app = Celery('task_manager')

# 3. Read configuration starting with 'CELERY_' from settings.py
app.config_from_object('django.conf:settings', namespace='CELERY')

# 4. Automatically discover task functions in tasks.py across all Django apps
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Celery Debug Request: {self.request!r}')
