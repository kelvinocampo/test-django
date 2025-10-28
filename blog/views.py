from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import PostForm
from .models import Post 

def post_list(request):
    posts = Post.objects.all() 
    contexto = {
        'lista_posts': posts,
    }
    return render(request, 'blog/post_list.html', contexto)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug) 
    return render(request, 
                  'blog/post_detail.html', 
                  {'post': post})

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'  # Ruta a la plantilla HTML

    # URL a la que se redirige al usuario después de guardar el post
    # Usamos reverse_lazy porque se evalúa después de cargar las URLs
    success_url = reverse_lazy('blog:post_list') 

    # Sobreescribir el método para asignar el usuario logueado como autor
    def form_valid(self, form):
        # Asigna el usuario actualmente logueado (self.request.user)
        form.instance.author = self.request.user 
        return super().form_valid(form)