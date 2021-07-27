from django_filters import rest_framework as filters

from advertisements.models import Advertisement, AdvertisementStatusChoices


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    creator = 'creator__id'

    created_at = filters.DateFromToRangeFilter()

    status = filters.MultipleChoiceFilter(choices=AdvertisementStatusChoices.choices)

    favorites = 'favorites'

    class Meta:
        model = Advertisement
        fields = ['creator', 'created_at', 'status', 'favorites']
