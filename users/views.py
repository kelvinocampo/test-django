# users/views.py (O donde tengas definidas tus vistas de usuario)

from django.contrib.auth.models import User
from django.views.generic import DetailView, CreateView
from django.urls import reverse_lazy, reverse # ¡IMPORTAR REVERSE!
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin
# Asegúrate de importar tu formulario personalizado:
from .forms import CustomUserCreationForm 
from django.contrib.auth.views import LogoutView


class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class RegisterView(CreateView):
    # CORRECCIÓN CLAVE: Usar form_class en lugar de model y fields
    form_class = CustomUserCreationForm 
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    # Nota: El modelo sigue siendo User, pero el formulario lo maneja internamente


class UserDetailView(LoginRequiredMixin, DetailView):
    # FUNCIONA CORRECTAMENTE
    model = User 
    template_name = 'users/user_detail.html'
    context_object_name = 'perfil_usuario'
    slug_field = 'username'
    slug_url_kwarg = 'username'


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    # FUNCIONA CORRECTAMENTE
    model = User
    fields = ['email', 'first_name', 'last_name'] 
    template_name = 'users/user_update.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    
    def get_success_url(self):
        # CORRECCIÓN: Usar reverse() para generar la URL de éxito
        return reverse('user_detail', kwargs={'username': self.request.user.username})

    def test_func(self):
        # FUNCIONA CORRECTAMENTE: Asegura que solo se edite el perfil propio
        user_to_edit = self.get_object() 
        return self.request.user == user_to_edit