from django.urls import path, include
# from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter

from .views import TagViewSet, IngredientViewSet, RecipeViewSet


router = DefaultRouter()
router.register('tags', TagViewSet)
router.register('ingredients', IngredientViewSet)
router.register('recipe', RecipeViewSet)

app_name = 'recepe'

urlpatterns = [
    path('', include(router.urls)),
]
