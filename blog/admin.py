from django.contrib import admin
from .models import Post, User # Importamos el modelo que acabamos de crear

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_publicacion')
    list_display_links = ('titulo',)
    list_filter = ('fecha_publicacion', 'autor')
    search_fields = ('titulo', 'contenido')
    prepopulated_fields = {'slug': ('titulo',)} 

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'creador', 'fecha_creacion')
    list_display_links = ('nombre',)
    list_filter = ('fecha_creacion', 'nombre')
    search_fields = ('nombre', 'correo')
    prepopulated_fields = {'slug': ('nombre',)} 