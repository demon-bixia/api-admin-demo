import logging

from celery import shared_task

from django.contrib.auth.models import User
from django.core.management import call_command

from blog.models import Author, Book

logger = logging.getLogger(__name__)


@shared_task
def create_user():
    try:
        User.objects.all().delete()
        user = User.objects.create(
            email='admin@example.com',
            username='admin',
            first_name='Admin',
            last_name='User'
        )
        user.set_password("password")
        logger.info(f"Demo user created successfully")
    except Exception as e:
        logger.error(f"Failed to create demo user: {e}")
        return f"Failed to create demo user: {e}"


@shared_task
def load_fixtures():
    try:
        Book.objects.all().delete()
        Author.objects.all().delete()
        call_command("loaddata", "authors.json", "books.json")
        logger.info(f"Successfully loaded data")
        return f"Loaded authors, and books initial data successfully."
    except Exception as e:
        logger.error(f"Failed to load initial data, error: {e}")
        return f"Failed to load initial data, error: {e}"
