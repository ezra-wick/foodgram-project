from .models import (Ingredient,
                     IngredientRecipe)
from django.db import IntegrityError, transaction
from django.http import HttpResponseBadRequest


def get_ingredients(request):
    ingredients = {}
    for key in dict(request.POST.items()):
        if 'nameIngredient' in key:
            name_of_ingridient = key.split('_')
            ingredients[dict(request.POST.items())[key]] = int(request.POST[
                f'valueIngredient_{name_of_ingridient[1]}'])

    return ingredients


def save_recipe(request, form, ingredients):
    try:
        with transaction.atomic():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            objs = []
            for name, quantity in ingredients.items():
                if quantity < 1:
                    form.add_error(None, "Кол-во ингридиентов не должно быть отрицательным")
                ingredient = Ingredient.objects.filter(title=name).first()
                objs.append(
                    IngredientRecipe(
                        recipe=recipe,
                        ingredient=ingredient,
                        amount=quantity
                    )
                )
            IngredientRecipe.objects.bulk_create(objs)
            form.save_m2m()
            return recipe
    except IntegrityError:
        raise HttpResponseBadRequest
