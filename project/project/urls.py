"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from .apps.webSite import views as webSite_views


urlpatterns = [
    path('', webSite_views.Index.as_view(), name='index'),
    path('test/', webSite_views.Test.as_view(), name='test'),
    path('motevaset/', webSite_views.Level_Motevasset.as_view(), name='motevaset'),
    path('momtaz/', webSite_views.Level_khosh.as_view(), name='momtaz'),
    path('khosh/', webSite_views.Level_Momtaz.as_view(), name='khosh'),
    path('awli/', webSite_views.Level_Awli.as_view(), name='awli'),
    path('content/',
         include('project.apps.fileManager.urls', namespace='content')),
    path('user/',
         include('project.apps.userManager.urls', namespace='user')),
    path('admin/', admin.site.urls),

]
