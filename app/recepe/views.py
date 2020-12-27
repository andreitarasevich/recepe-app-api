from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Tag
from recepe.serializers import TagSerializer


class TagViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """Manage tags in database"""
    authentication_classes = {TokenAuthentication, }
    permission_classes = {IsAuthenticated, }
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get_queryset(self):
        """return objects for authentificated user only"""
        return self.queryset.filter(user=self.request.user).order_by('-name')
