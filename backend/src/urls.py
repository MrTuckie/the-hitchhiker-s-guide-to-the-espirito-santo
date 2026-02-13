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
from django.urls import base, include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter

from apps.activity.api.views import ActivityViewSet
from apps.place.api.views import PlaceViewSet
from apps.post.api.views import PostViewSet
from apps.user_profile.api.views import GroupViewSet, UserViewSet, UserProfileViewSet
from apps.vote.api.views import VoteViewSet

ROUTER = DefaultRouter()
ROUTER.register(r"users", UserViewSet)  # OK
ROUTER.register(r"profiles", UserProfileViewSet)  # OK
ROUTER.register(r"groups", GroupViewSet)  # OK
ROUTER.register(r"places", PlaceViewSet)
ROUTER.register(r"posts", PostViewSet, basename="posts")
ROUTER.register(r"activities", ActivityViewSet)
ROUTER.register(r"votes", VoteViewSet, basename="votes")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/v1/", include(ROUTER.urls)),
    # YOUR PATTERNS
    path("api/v1/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path(
        "api/v1/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/v1/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
