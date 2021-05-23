import csv

from django.core.management.base import BaseCommand

from recipes.models import Ingredient, Tag


class Command(BaseCommand):
    help = 'Загрузка ингридиентов в БД'

    def handle(self, *args, **options):
        with open('data/ingredients.csv', encoding='utf-8') as file:
            file_reader = csv.reader(file)
            for ingredient in file_reader:
                Ingredient.objects.get_or_create(title=ingredient[0],
                                                 dimension=ingredient[1])

        with open('data/tags.csv', encoding='utf-8') as file:
            file_reader = csv.reader(file, engine='python')
            print(file_reader)
            for tags in file_reader:
                Tag.objects.get_or_create(title=tags[0],
                                          display_name=tags[1],
                                          color=tags[2])
