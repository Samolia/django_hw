from django.db import models


class TimestampFields(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # при этом флаге модель не будет использоваться для создания таблицы в БД.
                         # все поля этой модели унаследуются дочерними классами.


class Project(TimestampFields):
    """Объект на котором проводят измерения."""

    name = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'проект'
        verbose_name_plural = 'проекты'


class Measurement(TimestampFields):
    """Измерение температуры на объекте."""

    value = models.FloatField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='media')

    def __str__(self):
        return f'{self.project} - {self.value}'

    class Meta:
        verbose_name = 'температура'
        verbose_name_plural = 'температура'
