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
        print(thing)
        ingredient = IngredientSerializer(thing, many=False)
        ingredients.append(ingredient.data)

    print(ingredients)

    fullsteps = recipe.data.get('steps')

    splitsteps = fullsteps.split('/n')

    context = {'recipe':recipe.data, 'ingredients': ingredients, 'steps':splitsteps}


    return render(request, 'recipe_info.html', context)

def submit_recipe(request):
    #Get values from html
    title = request.GET.get('title')
    servings = request.GET.get('servings')
    #ingredients_name = request.GET.get('name')
    #ingredients_amount = request.GET.get('amount')
    #ingredients_measurement = request.GET.get('measurement')
    steps = request.GET.get('steps')
    print(request.GET)
 #   print(len(request.GET))

    all_steps = ""
    count_steps = 1
    for key in request.GET:
        #Condense step inputs into single input?
        if "step" in key:
            step = request.GET.get("step_"+str(count_steps))
            print(step+"/n")
            all_steps+=step+"/n"
            count_steps+=1


    print(all_steps)
    id_r = Recipe.objects.all().count()

    Recipe.objects.create(id=id_r+1, user_id=0, title=title, servings=servings, steps=all_steps)

    query_r = Recipe.objects.all().filter(id=id_r+1)
    results_r = query_r.values()
    recipe = RecipeSerializer(results_r[0], many=False)
    r = Recipe(id=recipe.data.get('id'), user_id=recipe.data.get('user_id'), title=recipe.data.get('title'), steps=recipe.data.get('steps'), servings=recipe.data.get('servings'))

    ##Create Ingredient objects for each
    id_i = Ingredient.objects.all().count()

    for key in request.GET:
        print(key)
        #Create ingriedent object for all ingredients
        if "amount" in key:
            count = 0
            id_i += 1
            ingredients_amount=request.GET.get("amount_"+str(count))
            print(ingredients_amount)
            ingredients_measurement=request.GET.get("measurement_"+str(count))
            print(ingredients_measurement)
            ingredients_name=request.GET.get("name_"+str(count))
            print(ingredients_name)

            # Get all measurement objects to be put into Ingredient
            query_m = Measurement.objects.all().filter(type=ingredients_measurement)
            results_m = query_m.values()
            measurement = MeasurementSerializer(results_m[0], many=False)
            print(measurement)

            Ingredient.objects.create(id=id_i+1, name=ingredients_name, amount=ingredients_amount, measurement_id=measurement.data.get('id'), recipe_used=r)


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
    ingredients = []

    for thing in results_i:
        ingredient = IngredientSerializer(thing, many=False)
        ingredients.append(ingredient)

    fullsteps = recipe.data.get('steps')

    splitsteps = fullsteps.split('/n')

    context = {'recipe': recipe_data, 'ingredients': ingredients, 'steps': splitsteps}
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

