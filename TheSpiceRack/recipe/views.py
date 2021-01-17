from django.shortcuts import render
from .models import Ingredient, Recipe, Measurement
from .serializers import RecipeSerializer, IngredientSerializer, MeasurementSerializer
from rest_framework.response import Response
from django.shortcuts import render, redirect

#WHAT HAPPENS WHEN THEY WANT TO VIEW A SPECIFIC RECIPE
def view_recipe(request, recipe_id):
    #Search for specific recipe based on ID
    query = Recipe.objects.all().filter(id=recipe_id)
    results = query.values()
    recipe = RecipeSerializer(results[0], many=False)

    recipe_model = Recipe(id=recipe.data.get('id'), user_id=recipe.data.get('user_id'), title=recipe.data.get('title'), steps=recipe.data.get('steps'), servings=recipe.data.get('servings'))
    query_i = Ingredient.objects.all().filter(recipe_used=recipe_model)
    results_i = query_i.values()
    print(results_i)
    ingredients = []

    for thing in results_i:
        ingredient = IngredientSerializer(thing, many=False)
        ingredients.append(ingredient)

    print(ingredients)

    context = {'recipe':recipe.data, 'ingredients': ingredients}


    return render(request, 'recipe_info.html', context)

def submit_recipe(request):
    #Get values from html
    title = request.GET.get('title')
    servings = request.GET.get('servings')
    ingredients = request.GET.get('ingredients')
    steps = request.GET.get('steps')

    id_r = Recipe.objects.all().count()

    Recipe.objects.create(id=id_r+1, user_id=0, title=title, servings=servings, steps=steps)

    #Get all measurement objects to be put into Ingredient
    query_m = Measurement.objects.all()
    results_m = query_m.values()
    #TODO: Change to actually look for measurement before seralization
    measurement = MeasurementSerializer(results_m[0], many=False)

    query_r = Recipe.objects.all().filter(id=id_r+1)
    results_r = query_r.values()
    recipe = RecipeSerializer(results_r[0], many=False)
    r = Recipe(id=recipe.data.get('id'), user_id=recipe.data.get('user_id'), title=recipe.data.get('title'), steps=recipe.data.get('steps'), servings=recipe.data.get('servings'))

    ##Create Ingredient objects for each
    id_i = Ingredient.objects.all().count()
    Ingredient.objects.create(id=id_i+1, name=ingredients, amount=1, measurement_id=measurement.data.get('id'), recipe_used=r)

    return redirect('/users/')

def add_recipe(request):
    return render(request, 'add_recipe.html')


def edit_recipe(request, recipe_id):
    query = Recipe.objects.all().filter(id=recipe_id)
    results = query.values()
    recipe = RecipeSerializer(results[0], many=False)

    recipe_data = recipe.data
    recipe = Recipe(id=recipe_data.get('id'), title=recipe_data.get('title'), servings=recipe_data.get('servings'), steps=recipe_data.get('steps'))
    query_i = Ingredient.objects.all().filter(recipe_used=recipe)
    results_i = query_i.values()
    print(results_i)
    ingredients = []

    for thing in results_i:
        ingredient = IngredientSerializer(thing, many=False)
        ingredients.append(ingredient)

    context = {'recipe': recipe_data, 'ingredients': ingredients}
    #Upload results[0] into html values

    return render(request, 'edit_recipe.html', context)

def save_recipe(request, recipe_id):
    title = request.GET.get('title')
    servings = request.GET.get('servings')
    ingredients = request.GET.get('ingredients')
    steps = request.GET.get('steps')

    query_r = Recipe.objects.all().filter(id=recipe_id)
    results_r = query_r.values()
    recipe_preedit = RecipeSerializer(results_r[0], many=False)
    recipe_pre = Recipe(id=recipe_preedit.data.get('id'), user_id=recipe_preedit.data.get('user_id'), title=recipe_preedit.data.get('title'), servings=recipe_preedit.data.get('servings'), steps=recipe_preedit.data.get('steps'))

    recipe = Recipe(id=recipe_id, user_id=0, title=title, servings=servings, steps=steps)
    recipe.save()


    query_i = Ingredient.objects.all().filter(recipe_used=recipe_pre)
    results_i = query_i.values()
    ingredients = []

    for thing in results_i:
        ingredient = IngredientSerializer(thing, many=False)
        ingred = Ingredient(id=ingredient.data.get('id'), name=ingredient.data.get('name'), amount=ingredient.data.get('amount'), measurement_id=ingredient.data.get('measurement_id'), recipe_used=recipe)
        ingred.save()

    return redirect('/users/')


def delete_recipe(request, recipe_id):
    instance = Recipe.objects.get(id=recipe_id)
    instance.delete()
    return redirect('/users/')
