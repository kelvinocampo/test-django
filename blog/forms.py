from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        # Puedes usar '__all__' para incluir todos los campos si es necesario