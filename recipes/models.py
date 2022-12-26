from django.db import models
from datetime import datetime

# Create your models here.
class Recipe(models.Model):
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Receita'
        verbose_name_plural = 'Receitas'

    name = models.CharField(
        max_length=50
    )
    name.verbose_name = 'Nome'

    ingredients = models.TextField(
        max_length=1000
    )
    ingredients.verbose_name = 'Ingredientes'

    prepare_mode = models.TextField(
        max_length=1000
    )
    prepare_mode.verbose_name = 'Modo de preparo'

    preparation_time = models.IntegerField()
    preparation_time.verbose_name = 'Tempo de preparo'

    portions = models.IntegerField()
    portions.verbose_name = 'Porções'

    category = models.CharField(max_length=50)
    category.verbose_name = 'Categoria'

    created_at = models.DateTimeField(default=datetime.now, blank=True, editable=False)
    created_at.verbose_name = 'Criado em'


