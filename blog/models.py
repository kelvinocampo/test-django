# blog/models.py
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 

class Post(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE) 
    titulo = models.CharField(max_length=200) 
    contenido = models.TextField() 
    fecha_publicacion = models.DateTimeField(default=timezone.now) 
    slug = models.SlugField(unique=True, max_length=200) 

    class Meta:
        ordering = ['-fecha_publicacion'] 

    def __str__(self):
        return self.titulo