from django.shortcuts import render

from recipes.models import Recipe

# Create your views here.
def index(request):   
    recipes = Recipe.objects.all()

    context = {
        'recipes': recipes
    } 

    return render(request, 'recipes/index.html', context)

def recipe(request):
    return render(request, 'recipes/recipe.html')