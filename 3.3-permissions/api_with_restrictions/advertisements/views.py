from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .filters import AdvertisementFilter
from .models import Advertisement
from .permissions import IsAuthOrReadOnly, IsOwnerOrAdmin
from .serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ['destroy', 'update', 'partial_update']:
            return [IsAuthOrReadOnly(), IsOwnerOrAdmin()]
        elif self.action == 'create':
            return [IsAuthenticated()]
        return []

    def get_queryset(self):
        queryset = Advertisement.objects.filter(status__in=['OPEN', 'CLOSED'])
        if self.request.user.is_authenticated:
            draft = Advertisement.draft_objects.filter(creator=self.request.user)
            if not draft and self.action == 'list':
                raise NotFound({'detail': 'У вас нет объявлений в черновиках'})
            return queryset | draft
        return queryset
