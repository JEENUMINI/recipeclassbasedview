from django.forms import ModelForm
from recipes.models import Recipe
from django import forms

class CreateRecipeForm(ModelForm):
    ingredients=forms.CharField(widget=forms.Textarea)
    class Meta:
        model=Recipe
        fields=["recipe_name","ingredients","category","recipe_image","created_by"]