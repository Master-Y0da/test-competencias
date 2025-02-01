
from rest_framework import serializers
from .models import Plato
from api.v1.ingrediente.models import Ingrediente


class PlatoSerializer(serializers.ModelSerializer):

    ingredients = serializers.PrimaryKeyRelatedField(
        queryset=Ingrediente.objects.all(), 
        many=True)
    
    is_vegan = serializers.BooleanField(read_only=True)
    is_gluten_free = serializers.BooleanField(read_only=True)
    is_kosher = serializers.BooleanField(read_only=True)
    
    class Meta:
        model = Plato
        fields = '__all__'