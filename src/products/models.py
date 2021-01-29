from django.db import models
from django.urls import reverse

class Product(models.Model):
    title       = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(max_digits=10000, decimal_places=2)
    summary     = models.TextField()
    featured    = models.BooleanField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("products:product_detail", kwargs={"product_id": self.id})

    def is_featured(self):
        return 'yes' if self.featured else 'no'
