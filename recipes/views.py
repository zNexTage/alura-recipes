from django.shortcuts import render, get_object_or_404

from recipes.models import Recipe

# Create your views here.
def index(request):   
    recipes = Recipe.objects.all()

    context = {
        'recipes': recipes
    } 

    return render(request, 'recipes/index.html', context)

def recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)

    context = {
        'recipe': recipe
    }

    return render(request, 'recipes/recipe.html', context)