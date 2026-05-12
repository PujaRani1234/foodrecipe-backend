from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('create/', views.create_recipe, name='create_recipe'),
    path('update/<int:id>/', views.update_recipe, name='update_recipe'),
    path('delete/<int:id>/', views.delete_recipe, name='delete_recipe'),
]
