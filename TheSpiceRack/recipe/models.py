from django.db import models

# Create your models here.
class Measurement(models.Model):
    Tbsp = 'Tablespoon'
    tbsp = 'Teaspoon'
    oz = 'Ounces'
    cup = 'Cup'
    pint = 'Pint'
    quart = 'Quart'
    gallon = 'Gallon'
    mL = 'Milliliter'
    L = 'Liter'
    lb = 'Pound'
    g = 'Gram'
    Kg = 'Kilogram'

    MEASUREMENT_CHOICES = ((tbsp, tbsp),
        (Tbsp, Tbsp),
        (oz, oz),
        (cup, cup),
        (pint, pint),
        (quart, quart),
        (gallon, gallon),
        (mL, mL),
        (L, L),
        (lb, lb),
        (g, g),
        (Kg,Kg))

    #Primary Key
    id = models.IntegerField()
    type = models.CharField(max_length=200, choices=MEASUREMENT_CHOICES, default=tbsp)
    is_fluid = models.BooleanField()
    is_metric = models.BooleanField()

    def __str__(self):
        return self.type

class Ingredient(models.Model):
    #Primary Key
    id = models.IntegerField()
    name = models.CharField(max_length=200)
    amount = models.CharField(max_length=200)
    #Foreign Key
    measurement = models.ManyToOneRel(Measurement)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    # Primary Key
    id = models.IntegerField()
    user_id = models.IntegerField()
    title = models.CharField(max_length=200)
    steps = models.CharField()
    # Foreign Key
    ingredients = models.ManyToManyRel(Ingredient)

    def __str__(self):
        return self.title