from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework

from .models import Advertisement
from .serializers import AdvertisementSerializer


# Фильтрация объявлений по создателю и дате создания
class DataFilter(rest_framework.FilterSet):
    created_at = rest_framework.filters.DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['creator','created_at']


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = DataFilter


    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update"]:
            return [IsAuthenticated()]
        return []
