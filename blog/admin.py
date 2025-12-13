from django_api_admin import APIModelAdmin
from django_api_admin.sites import site
from .models import Author, Book


class AuthorModelAdmin(APIModelAdmin):
    view_on_site = False


site.register(Author, AuthorModelAdmin)
site.register(Book)
