from django_api_admin import APIModelAdmin
from django_api_admin.sites import site
from .models import Author, Book


class AuthModelAdmin(APIModelAdmin):
    view_on_site = False


site.register(Author, AuthModelAdmin)
site.register(Book)
