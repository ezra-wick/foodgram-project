from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

User = get_user_model()


class Ingredient(models.Model):
    title = models.CharField(max_length=200, null=True,
                             blank=True, db_index=True,
                             verbose_name="Ингредиент")
    dimension = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = 'ингредиент'
        verbose_name_plural = 'ингредиенты'

    def __str__(self):
        return f'{self.title} {self.dimension}'


class IngredientRecipe(models.Model):
    recipe = models.ForeignKey(
        'Recipe',
        on_delete=models.CASCADE,
        related_name='recipe_ingredients',
        verbose_name="Рецепт")
    ingredient = models.ForeignKey(
        'Ingredient',
        on_delete=models.CASCADE,
        related_name='recipe_ingredients',
        verbose_name="Ингредиент")
    amount = models.DecimalField(max_digits=6,
                                 decimal_places=0,
                                 validators=[MinValueValidator(1)]
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['ingredient', 'recipe'],
                                    name='unique ingredient and recipe')
        ]
        verbose_name = 'ингредиент рецепта'
        verbose_name_plural = 'ингредиенты рецепта'

    def __str__(self):
        return f'{self.ingredient.title} \
                 {self.amount} \
                 {self.ingredient.dimension}'


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name="Автор")
    title = models.CharField(max_length=200, verbose_name="Название")
    image = models.ImageField(
        upload_to='recipes/',
        blank=True,
        null=True,
        verbose_name="Картинка"
    )
    description = models.TextField(verbose_name="Описание")
    ingredients = models.ManyToManyField(
        'Ingredient',
        related_name='recipes',
        through='IngredientRecipe',
        verbose_name='Ингредиент'
    )
    cooking_time = models.PositiveIntegerField(
        verbose_name="Время приготовления, мин"
    )
    pub_date = models.DateTimeField(
        'date published',
        auto_now_add=True)
    tags = models.ManyToManyField(
        'Tag',
        related_name='recipes',
        verbose_name='Теги'
    )

    class Meta:
        ordering = ('-pub_date', )
        verbose_name = 'рецепт'
        verbose_name_plural = 'рецепты'

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField('Имя тега', max_length=50, db_index=True)
    display_name = models.CharField('Имя тега для шаблона', max_length=50)
    color = models.CharField('Цвет тега', max_length=50)

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'

    def __str__(self):
        return self.title


class FollowRecipe(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower_recipe')
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='following_recipe')

    def __str__(self):
        return f'follower - {self.user} following recipe - {self.recipe}'


class FollowUser(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'author'],
                                    name='unique together')
        ]

    def __str__(self):
        return f'follower - {self.user} following - {self.author}'


class ShopingList(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_shoping_list')
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='recipe_shoping_list')
