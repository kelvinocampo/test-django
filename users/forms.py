from django.contrib.auth.forms import UserCreationForm
# get_user_model() obtiene el modelo de usuario activo, por defecto django.contrib.auth.models.User
from django.contrib.auth import get_user_model 

# Obtenemos el modelo User que Django usa
User = get_user_model() 

class CustomUserCreationForm(UserCreationForm):
    """
    Formulario personalizado de creación de usuario que hereda de UserCreationForm.
    Esto permite añadir campos fácilmente (como el email) sin reescribir la lógica de contraseña.
    """
    class Meta:
        model = User
        # Definimos los campos que aparecerán en el formulario de registro:
        # username, email, password (y su confirmación, que son heredados automáticamente)
        fields = ('username', 'email')