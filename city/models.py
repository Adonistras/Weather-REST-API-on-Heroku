from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='City')
    country = models.CharField(max_length=50, blank=True, verbose_name='Country')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        ordering = ['-created']


