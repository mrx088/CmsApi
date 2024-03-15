from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    price = models.IntegerField()
    count = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='products/%Y/%m/%d/',blank=True,null=True)
    popularity = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    colors = models.SmallIntegerField()
    sale = models.IntegerField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title