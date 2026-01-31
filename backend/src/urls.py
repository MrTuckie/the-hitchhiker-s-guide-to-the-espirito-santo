"""
URL configuration for src project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from apps.place.api.views import PlaceViewSet
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets, serializers
from apps.user_profile.api.views import UserViewSet, GroupViewSet

from apps.post.api.views import PostViewSet
from apps.activity.api.views import ActivityViewSet
from apps.vote.api.views import VoteViewSet

ROUTER = DefaultRouter()
ROUTER.register(r"users", UserViewSet)  # OK
ROUTER.register(r"groups", GroupViewSet)  # OK
ROUTER.register(r"places", PlaceViewSet)
ROUTER.register(r"posts", PostViewSet)
ROUTER.register(r"activities", ActivityViewSet)
ROUTER.register(r"votes", VoteViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/v1/", include(ROUTER.urls)),
]
