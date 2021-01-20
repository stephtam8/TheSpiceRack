from django import forms
from . import models

class AddRecipeForm(forms.Form):
    title = forms.CharField(help_text='Title of Recipe')
    #steps = forms.CharField(help_text='Steps of Recipe')
    servings = forms.IntegerField(help_text='Number of servings in Recipe')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #User can add as many ingredient fields as needed
        ingredients = models.Ingredient.objects.filter(
            ingredient=self.instance
        )
        for i in range(len(ingredients) + 1):
            field_name = 'ingredient_%s' % (i,)
            self.fields[field_name] = forms.CharField(required=False)
            try:
                self.initial[field_name] = ingredients[i].ingredient
            except IndexError:
                self.initial[field_name] = ""
                # create an extra blank field
                field_name = 'ingredient_%s' % (i + 1,)
                self.fields[field_name] = forms.CharField(required=False)

        #User can add as many steps as needed
        steps = models.RecipeStep.objects.filter(
            step=self.instance
        )
        for i in range(len(steps) + 1):
            field_name = 'step_%s' % (i,)
            self.fields[field_name] = forms.CharField(required=False)
            try:
                self.initial[field_name] = steps[i].step
            except IndexError:
                self.initial[field_name] = ""
                # create an extra blank field
                field_name = 'step_%s' % (i + 1,)
                self.fields[field_name] = forms.CharField(required=False)
