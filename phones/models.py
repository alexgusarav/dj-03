from django.db import models


class Phone(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=50, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    image = models.URLField(max_length=200, null=True)
    release_date = models.DateField(null=True)
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(max_length=50, null=True)
