from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from core.models import Recipe, Tag, Ingredient
from recipe.serializers import TagSerializer, IngredientSerializer
from recipe.serializers import RecipeSerializer


class BaseRecipeAttrViewSet(viewsets.GenericViewSet,
                            mixins.ListModelMixin,
                            mixins.CreateModelMixin):
    """Base viewset for user owned recipe attributes"""
    authentication_classes = {TokenAuthentication, }
    permission_classes = {IsAuthenticated, }

    def get_queryset(self):
        """Return objects for the current authentificated user only"""
        return self.queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self, serializer):
        """Create a new object"""
        serializer.save(user=self.request.user)


class TagViewSet(BaseRecipeAttrViewSet):
    """Manage tags in database"""
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class IngredientViewSet(BaseRecipeAttrViewSet):
    """Manage ingredients in the database"""
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    """Manage recipes in database"""
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    authentication_classes = (
        TokenAuthentication,
    )
    permission_classes = (
        IsAuthenticated,
    )

    def get_queryset(self):
        """Retrive the recipies for authentificated user"""
        return self.queryset.filter(user=self.request.user)
