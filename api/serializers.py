from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from recipes.models import FollowRecipe, FollowUser, Ingredient, ShopingList


class CustomModelSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return self.Meta.model.objects.create(**validated_data)


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('title', 'dimension')
        model = Ingredient


class SubscriptionSerializer(CustomModelSerializer):
    class Meta:
        fields = ('author', )
        model = FollowUser

    def validate_author(self, value):
        user = self.context['request'].user
        if user.id == value:
            raise ValidationError('Нельзя подписаться на самого себя')
        return value


class FavoriteSerializer(CustomModelSerializer):
    class Meta:
        fields = ('recipe', )
        model = FollowRecipe


class PurchaseSerializer(CustomModelSerializer):
    class Meta:
        fields = ('recipe', )
        model = ShopingList
