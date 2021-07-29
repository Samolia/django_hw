from django.conf import settings
from django.db import models


class AdvertisementStatusChoices(models.TextChoices):
    """Статусы объявления."""

    OPEN = 'OPEN', 'Открыто'
    CLOSED = 'CLOSED', 'Закрыто'
    DRAFT = 'DRAFT', 'Черновик'


class DraftAdvertisementManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='DRAFT')


class Advertisement(models.Model):
    """Объявление."""

    title = models.TextField(verbose_name='Название объявления')
    description = models.TextField(default='', verbose_name='Описание')
    status = models.TextField(
        choices=AdvertisementStatusChoices.choices,
        default=AdvertisementStatusChoices.OPEN, verbose_name='Статус'
    )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, verbose_name='Автор'
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    objects = models.Manager()
    draft_objects = DraftAdvertisementManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
