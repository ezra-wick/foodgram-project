from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
from rest_framework.utils import json

from recipes.models import (FollowRecipe, FollowUser, Ingredient, Recipe,
                            ShopingList)


class IngredientApi(LoginRequiredMixin, View):
    def get(self, request):
        text = request.GET['query'] or None
        ingredients = list(Ingredient.objects.filter(
            title__icontains=text).values('title', 'dimension'))
        return JsonResponse(ingredients, safe=False)


class Favorites(LoginRequiredMixin, View):
    def post(self, request):
        req = json.loads(request.body)
        # Я не понял(
        recipe_id = req.get('id', None)
        if recipe_id:
            recipe = get_object_or_404(Recipe, id=recipe_id)
            _, created = FollowRecipe.objects.get_or_create(
                user=request.user, recipe=recipe
            )
            # вы наверное не это имели ввиду, но по другому у меня ошибка
            return JsonResponse(
                {'success': True} if created else {'success': False})
        return JsonResponse({'success': False}, status=400)

    def delete(self, request, recipe_id):
        recipe = get_object_or_404(
            FollowRecipe, recipe=recipe_id, user=request.user
        )
        recipe.delete()
        return JsonResponse({'success': True})


class Subscribe(LoginRequiredMixin, View):
    def post(self, request):
        req = json.loads(request.body)
        author_id = req.get('id', None)
        if author_id is not None:
            author = get_object_or_404(User, id=author_id)
            _, created = FollowUser.objects.get_or_create(
                user=request.user, author=author
            )
            return JsonResponse(
                {'success': True} if created else {'success': False})
        return JsonResponse({'success': False}, status=400)

    def delete(self, request, author_id):
        obj = get_object_or_404(
            FollowUser,
            user__username=request.user.username,
            author__id=author_id)
        obj.delete()
        return JsonResponse({'success': True})


class Purchase(LoginRequiredMixin, View):
    def post(self, request):
        # Я не понял(
        recipe_id = json.loads(request.body)['id']
        recipe = get_object_or_404(Recipe, id=recipe_id)
        ShopingList.objects.get_or_create(user=request.user, recipe=recipe)
        return JsonResponse({'success': True})

    def delete(self, request, recipe_id):
        obj = get_object_or_404(
            ShopingList,
            user__username=request.user.username,
            recipe__id=recipe_id)
        obj.delete()
        return JsonResponse({'success': True})
