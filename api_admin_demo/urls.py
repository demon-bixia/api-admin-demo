"""
URL configuration for api_admin_demo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django_api_admin.sites import site
from blog.views import demo_user, load_fixtures, migrate

urlpatterns = [
    path('admin/', site.urls),
    path('management/fixtures/', load_fixtures),
    path('management/migrate/', migrate),
    path('management/demo-user/', demo_user),
]
