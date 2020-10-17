from datetime import timedelta
from celery.schedules import crontab


schedule_name = 'beat_push'
task_path = 'books.tasks.push_book'
schedule_time = 5
schedule_queue = 'worker_queue'


CELERYBEAT_SCHEDULE = {
    schedule_name: {
        'task': task_path,
        'schedule': timedelta(seconds=schedule_time),
        'options': {
            'queue': schedule_queue,
        }
    }
}