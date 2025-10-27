# blog/admin.py

from django.contrib import admin
from .models import Post # Importamos el modelo que acabamos de crear

# Opción 1: Registro simple
# admin.site.register(Post)

# Opción 2: Registro avanzado (recomendado para mejor interfaz)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Campos que se muestran en la lista del panel:
    list_display = ('titulo', 'autor', 'fecha_publicacion')
    
    # Campos que se convierten en enlaces a la página de edición:
    list_display_links = ('titulo',)
    
    # Campos que se pueden filtrar en el panel lateral:
    list_filter = ('fecha_publicacion', 'autor')
    
    # Campos que se pueden buscar:
    search_fields = ('titulo', 'contenido')
    
    # Pre-pobla el campo 'slug' automáticamente a partir del campo 'titulo'
    prepopulated_fields = {'slug': ('titulo',)} 

# Nota: Hemos eliminado el registro simple si usamos la opción avanzada con el decorador @admin.register