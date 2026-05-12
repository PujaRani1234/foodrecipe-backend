
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe
from .forms import RecipeForm

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipelist.html', {'recipes': recipes})

def create_recipe(request):
    form = RecipeForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('recipe_list')

    return render(request, 'recipeform.html', {
        'form': form,
        'page_title': 'Add Recipe',
        'submit_label': 'Save recipe',
    })

def update_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    form = RecipeForm(request.POST or None, instance=recipe)

    if form.is_valid():
        form.save()
        return redirect('recipe_list')

    return render(request, 'recipeform.html', {
        'form': form,
        'page_title': 'Edit Recipe',
        'submit_label': 'Update recipe',
    })

def delete_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    recipe.delete()
    return redirect('recipe_list')