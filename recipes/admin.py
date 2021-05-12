from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple

from recipes.models import (FollowRecipe, FollowUser, Ingredient,
                            IngredientRecipe, Recipe, ShopingList, Tag)


class IngredientRecipeInline(admin.TabularInline):
    model = IngredientRecipe
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'pub_date', 'description')
    search_fields = ('decsription',)
    list_filter = ('pub_date',)
    inlines = (IngredientRecipeInline,)
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }


admin.site.register(Recipe, RecipeAdmin)


class IngredientsAdmin(admin.ModelAdmin):
    list_display = ('title', 'dimension',
                    'description')
    list_filter = ('title',)
    search_fields = ('title',)
    inlines = (IngredientRecipeInline,)


admin.site.register(Ingredient, IngredientsAdmin)


class ShopingListAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')
    list_filter = ('user',)
    search_fields = ('user',)


admin.site.register(ShopingList, ShopingListAdmin)


class FlUsAdmin(admin.ModelAdmin):
    list_display = ('user', 'author')
    list_filter = ('user',)
    search_fields = ('user',)


admin.site.register(FollowUser, FlUsAdmin)


class FlRecAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')
    list_filter = ('user',)
    search_fields = ('recipe',)


admin.site.register(FollowRecipe, FlRecAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'color', 'display_name')
    list_filter = ('title', )


admin.site.register(Tag, TagAdmin)
