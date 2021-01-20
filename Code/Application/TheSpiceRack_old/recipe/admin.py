from django.contrib import admin
from .models import Recipe, RecipeStep, Measurement, Ingredient

# Register your models here.
admin.site.register(Recipe)
admin.site.register(RecipeStep)
admin.site.register(Measurement)
admin.site.register(Ingredient)
