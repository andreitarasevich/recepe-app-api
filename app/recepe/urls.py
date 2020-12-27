from django.urls import path, include
# from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter

from .views import TagViewSet


router = DefaultRouter()
router.register('tags', TagViewSet)

app_name = 'recepe'

urlpatterns = [
    path('', include(router.urls)),
]
