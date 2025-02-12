import logging

from django.core.management.base import BaseCommand, CommandError
from django_celery_beat.models import PeriodicTask, IntervalSchedule

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Delete the tasks used to populate the database with demo data"

    def handle(self, *args, **options):
        try:
            PeriodicTask.objects.filter(name="creating the demo user").delete()
            PeriodicTask.objects.filter(name="load the demo data").delete()
            IntervalSchedule.objects.all().delete()
        except Exception as e:
            logger.error(
                f"An error occurred while removing scheduling periodic tasks: {e}")
            raise CommandError(
                f'An error occurred while removing scheduling periodic tasks: {e}')
