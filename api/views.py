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
        text = request.GET.get('query')
        if text is not None:
            ingredients = list(Ingredient.objects.filter(
                title__icontains=text).values('title', 'dimension'))
            return JsonResponse(ingredients, safe=False)
        return JsonResponse({'success': False}, status=400)


class Favorites(LoginRequiredMixin, View):
    def post(self, request):
        req = json.loads(request.body)
        recipe_id = req.get('id')
        if recipe_id is not None:
            recipe = get_object_or_404(Recipe, id=recipe_id)
            _, created = FollowRecipe.objects.get_or_create(
                user=request.user, recipe=recipe
            )
            return JsonResponse({'success': created})
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
        author_id = req.get('id')
        if author_id:
            author = get_object_or_404(User, id=author_id)
            _, created = FollowUser.objects.get_or_create(
                user=request.user, author=author
            )
            return JsonResponse({'success': created})
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
        req = json.loads(request.body)
        recipe_id = req.get('id')
        if recipe_id is not None:
            recipe = get_object_or_404(Recipe, id=recipe_id)
            ShopingList.objects.get_or_create(user=request.user, recipe=recipe)
            return JsonResponse({'success': True})

        return JsonResponse({'success': False}, status=400)

    def delete(self, request, recipe_id):
        obj = get_object_or_404(
            ShopingList,
            user__username=request.user.username,
            recipe__id=recipe_id)
        obj.delete()
        return JsonResponse({'success': True})
