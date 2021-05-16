from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from django.db.models import Count, Sum
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from foodgram import settings

from .forms import RecipeForm
from .models import Recipe, ShopingList, Tag, User, IngredientRecipe
from .utils import get_ingredients, save_recipe

TAGS = ['breakfast', 'lunch', 'dinner']


def index(request):
    tags = request.GET.getlist('tag', TAGS)
    all_tags = Tag.objects.all()
    recipes = Recipe.objects.filter(
        tags__title__in=tags
    ).select_related(
        'author'
    ).prefetch_related(
        'tags'
    ).distinct()
    paginator = Paginator(recipes, settings.PAGINATE_BY)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(
        request, 'index.html', {
            'page': page,
            'paginator': paginator,
            'tags': tags,
            'all_tags': all_tags,
        }
    )


def profile(request, username):
    tags = request.GET.getlist('tag', TAGS)
    all_tags = Tag.objects.all()
    author = get_object_or_404(User, username=username)
    author_recipes = author.recipes.filter(
        tags__title__in=tags
    ).prefetch_related('tags').distinct()

    paginator = Paginator(author_recipes, settings.PAGINATE_BY)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'authorRecipe.html',
                  {
                      'page': page,
                      'paginator': paginator,
                      'username': author,
                      'tags': tags,
                      'all_tags': all_tags,
                  }
                  )


def recipe_view(request, recipe_id, username):
    recipe = get_object_or_404(
        Recipe.objects.select_related('author'),
        id=recipe_id)
    ingredients = IngredientRecipe.objects.filter(recipe=recipe)
    return render(request, 'singlePage.html', {'recipe': recipe,
                                                'username': username,
                                                'ingredients': ingredients})


@login_required
def new_recipe(request):
    form = RecipeForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        recipe = save_recipe(request, form)
        return redirect(
            'recipe_view', recipe_id=recipe.id, username=recipe.author
        )
    return render(request, 'formRecipe.html', {'form': form})


@login_required
def recipe_edit(request, username, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    ingredients = get_ingredients(request)
    form = RecipeForm(request.POST or None,
                      files=request.FILES or None,
                      instance=recipe)
    if not request.user.is_superuser or request.user == recipe.author:
        if form.is_valid():
            recipe = save_recipe(request, form)
            return redirect(
                'recipe_view', recipe_id=recipe.id, username=recipe.author
            )
    return render(request, 'formRecipe.html',
                  {'form': form, 'recipe': recipe})


@login_required
def recipe_delete(request, username, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.user.is_superuser or request.user == recipe.author:
        recipe.delete()
    return redirect('index')


@login_required
def follow_index(request):
    follow = User.objects.filter(
        following__user=request.user
    ).prefetch_related(
        'recipes'
    ).annotate(recipe_count=Count('recipes')).order_by('username')
    paginator = Paginator(follow, settings.PAGINATE_BY)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'myFollow.html', {
        'page': page,
        'paginator': paginator,
        'follow': follow,
    }
    )


@login_required
def favorite_index(request):
    tags = request.GET.getlist('tag', TAGS)
    all_tags = Tag.objects.all()

    recipes = Recipe.objects.filter(
        following_recipe__user=request.user,
        tags__title__in=tags
    ).select_related(
        'author'
    ).prefetch_related(
        'tags'
    ).distinct()
    paginator = Paginator(recipes, settings.PAGINATE_BY)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'favorite.html', {
        'page': page,
        'paginator': paginator,
        'tags': tags,
        'all_tags': all_tags,
    }
    )


@login_required
def shopping_list(request):
    shopping_list = ShopingList.objects.filter(user=request.user)
    return render(
        request,
        'shopList.html',
        {'shopping_list': shopping_list}
    )


@login_required
def download_card(request):
    recipes = Recipe.objects.filter(recipe_shoping_list__user=request.user)
    ingredients = recipes.values(
        'ingredients__title', 'ingredients__dimension'
    ).annotate(
        total_amount=Sum('recipe_ingredients__amount')
    )
    file_data = 'Список покупок:\n'

    for item in ingredients:
        line = ' '.join(str(value) for value in item.values())
        if line != 'None None None':
            file_data += line + '\n'

    response = HttpResponse(
        file_data, content_type='application/text charset=utf-8'
    )
    filename = 'shopping_list.txt'
    response['Content-Disposition'] = ('attachment; filename={0}'
                                      .format(filename))
    return response
