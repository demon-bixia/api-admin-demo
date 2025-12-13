import logging

from django.core.management.base import BaseCommand, CommandError
from django_celery_beat.models import PeriodicTask, IntervalSchedule

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Schedules the celery tasks that update the demo data"

    def handle(self, *args, **options):
        try:
            schedule, _created = IntervalSchedule.objects.get_or_create(
                every=5,
                period=IntervalSchedule.MINUTES,
            )
            PeriodicTask.objects.create(
                interval=schedule,
                name='creating the demo user',
                task='blog.tasks.create_user',
            )
            PeriodicTask.objects.create(
                interval=schedule,
                name='load the demo data',
                task='blog.tasks.load_fixtures',
            )
            logger.info("Periodic tasks scheduled successfully")

        except Exception as e:
            logger.error(
                f"An error occurred when scheduling periodic tasks: {e}")
            raise CommandError(
                f'An error occurred when scheduling periodic tasks: {e}')
