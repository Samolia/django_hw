from django.db import models


class Phone(models.Model):
    name = models.TextField()
    price = models.FloatField()
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()

    def __str__(self):
        return f'{self.id}; {self.name}; {self.price}; {self.image};' \
               f'{self.release_date}; {self.lte_exists}; {self.slug}'
