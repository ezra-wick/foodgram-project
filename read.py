#@user_passes_test(lambda u: u.is_superuser)
from recipes.models import Ingredients

def add_ingredients():
    import json
    from django.http import HttpResponse

    with open('ingredients.json', 'r') as fh:
        data = json.load(fh)

    for i in data:
        print('You added this new ingredient:', i)
        ingredient = Ingredients(title=i['title'], dimension=i['dimension'])
        ingredient.save()
    return HttpResponse('\n'.join(str(data)))


add_ingredients()