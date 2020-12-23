"""RecipeClass URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import CreateRecipe,ListRecipes,RecipeEdit,RecipeView,RecipeDelete,AllRecipes

urlpatterns = [

path('createrecipe',CreateRecipe.as_view(),name="createrecipe"),
path('listrecipe',ListRecipes.as_view(),name="listrecipe"),
path('recipeedit/<int:pk>',RecipeEdit.as_view(),name="recipeedit"),
path('recipeview/<int:pk>',RecipeView.as_view(),name="recipeview"),
path('recipedelete/<int:pk>',RecipeDelete.as_view(),name="recipedelete"),
path('allrecipe',AllRecipes.as_view(),name="allrecipe"),
]
