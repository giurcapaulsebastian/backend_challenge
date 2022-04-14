from django.db import models

# Create your models here.

class Product(models.Model):
    status_choices = [
        ('ACTIVE', 'ACTIVE'),
        ('INACTIVE', 'INACTIVE'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=status_choices, default='ACTIVE')

    def __str__(self):
        return self.name

class Nutrition(models.Model):
    unit_choices = [
        ('g', 'gram'),
        ('Kcal', 'kcal'),
    ]
    name_choices = [
        ('Protein', 'Protein'),
        ('Carbohydrate', 'Carbohydrate'),
        ('Fat', 'Fat'),
        ('Sugar', 'Sugar'),
        ('Fiber', 'Fiber'),
        ('Energetic Value', 'Energetic Value'),
    ]
    name = models.CharField(max_length=100, choices=name_choices)
    unit = models.CharField(max_length=5, choices=unit_choices)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    value = models.DecimalField(default=0.00,max_digits=7,decimal_places=2)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'product'], name='unique_nutrition_product')
        ]

    def __str__(self):
        return self.name