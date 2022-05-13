from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
