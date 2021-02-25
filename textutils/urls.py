"""textutils URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("one", views.one, name="one"),
    path("GFG", views.GFG, name="GFG"),
    path("www_dcwh", views.www_dcwh, name="www_dcwh"),
    path("oo1_gmail", views.oo1_gmail, name="oo1_gmail"),
    path("opti_mail", views.opti_mail, name="opti_mail")


]
