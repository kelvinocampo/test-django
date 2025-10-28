# blog/serializers.py

from rest_framework import serializers
from .models import Post # Importa tu modelo Post

class PostSerializer(serializers.ModelSerializer):
    # Opcional: El campo 'autor' es una FK, así lo mostramos como el username
    autor = serializers.ReadOnlyField(source='autor.username')

    class Meta:
        model = Post
        # Define qué campos del modelo quieres exponer en la API
        fields = ['id', 'titulo', 'contenido', 'autor', 'fecha_publicacion', 'slug']
        # O usa fields = '__all__' para incluir todos los campos.