from django.db import models
from api.v1.ingrediente.models import Ingrediente


class Plato(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.ManyToManyField(Ingrediente)

    @property
    def is_vegan(self):
        return all(item.is_vegan for item in self.ingredients.all())
    
    @property
    def is_gluten_free(self):
        return all(item.is_gluten_free for item in self.ingredients.all())
    
    @property
    def is_kosher(self):
        return all(item.is_kosher for item in self.ingredients.all())
    
    def __str__(self):
        return self.name
