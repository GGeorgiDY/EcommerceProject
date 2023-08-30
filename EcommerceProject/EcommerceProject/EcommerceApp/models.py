from django.db import models


CATEGORY_CHOICES = (
    ('CBDOil', 'CBD Oil'),
    ('CBDPaste', 'CBD Paste'),
    ('CBDDABWAX', 'CBD DAB WAX'),
    ('CBDVape', 'CBD Vape'),
    ('CBDCosmetics', 'CBD Cosmetics'),
)


class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField(
        blank=True,
        null=True,
    )
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(
        choices=CATEGORY_CHOICES,
        max_length=13,
    )
    product_image = models.ImageField(upload_to='product')

    def __str__(self):
        return self.title
