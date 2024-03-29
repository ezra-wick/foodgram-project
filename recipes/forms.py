from django import forms
from django.forms import CheckboxSelectMultiple

from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'title',
            'tags',
            'image',
            'description',
            'cooking_time']
        widgets = {
            'tags': CheckboxSelectMultiple(),
        }
