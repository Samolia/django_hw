from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='название')
    text = models.TextField(verbose_name='текст')
    published_at = models.DateTimeField(verbose_name='дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='изображение')
    tags = models.ManyToManyField('Tag', through='Scope', related_name='tag')

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=256)

    class Meta:
        verbose_name = 'раздел'
        verbose_name_plural = 'разделы'
        ordering = ['name']

    def __str__(self):
        return self.name


class Scope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='статья', related_name='scopes')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='раздел')
    is_main = models.BooleanField(verbose_name='основной')

    class Meta:
        verbose_name_plural = 'темы статьи'
        ordering = ['-is_main', 'tag']
