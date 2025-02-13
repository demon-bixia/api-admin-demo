from django.contrib.auth import get_user_model, models
from django.core.management import call_command

from rest_framework.decorators import api_view
from rest_framework.views import Response, status


from blog.models import Author, Book


@api_view(['GET'])
def migrate(request):
    # run migrations
    call_command('migrate')
    return Response({"detail":  "success"}, status=status.HTTP_200_OK)


@api_view(['GET'])
def demo_user(request):
    # create the demo user
    User = get_user_model()
    User.objects.all().delete()
    user = User.objects.create(
        email='admin@example.com',
        username='admin',
        first_name='Admin',
        last_name='User',
        is_superuser=True,
        is_staff=True
    )
    user.set_password("password")
    user.save()
    return Response({"detail":  "success"}, status=status.HTTP_200_OK)


@api_view(['GET'])
def load_fixtures(request):
    Book.objects.all().delete()
    Author.objects.all().delete()
    call_command("loaddata", "authors.json", "books.json")
    return Response({"detail":  "success"}, status=status.HTTP_200_OK)
