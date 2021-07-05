from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='titles of articles')
    text = models.TextField(verbose_name='the content of the article')
    published_at = models.DateTimeField(verbose_name='date of publication')
    image = models.ImageField(null=True, blank=True, verbose_name='image')
    tags = models.ManyToManyField('Tag', through='Scope', related_name='tag')

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'articles'
        ordering = ['-published_at']  # я же правильно понял, что если я здесь это указал, то во views.py
                                      # это будет сортировка по умолчанию?

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=256)

    class Meta:
        verbose_name = 'section'
        verbose_name_plural = 'sections'
        ordering = ['name']

    def __str__(self):
        return self.name


class Scope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='article')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='section')
    is_main = models.BooleanField(verbose_name='main')

    class Meta:
        verbose_name_plural = 'topics of article'
        ordering = ['-is_main', 'tag']
