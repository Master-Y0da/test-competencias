from django.db import models

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=255)
    is_vegan = models.BooleanField(default=False)
    is_gluten_free = models.BooleanField(default=False)
    is_kosher = models.BooleanField(default=False)


    def __str__(self):
        return self.nombre