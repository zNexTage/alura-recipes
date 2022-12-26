from django.urls import path
from recipes import views

app_name = 'recipes'

urlpatterns = [
    path('', views.index, name='index'),
    path('recipe/<int:pk>', views.recipe, name='recipe'),
]
