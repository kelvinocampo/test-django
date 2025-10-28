# blog/api/views.py

from rest_framework import viewsets
from ..models import Post
from ..serializers import PostSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
    """
    Este ViewSet proporciona automáticamente acciones para
    'list', 'create', 'retrieve', 'update', 'partial_update' y 'destroy'.
    """
    queryset = Post.objects.all().order_by('-fecha_publicacion')
    serializer_class = PostSerializer

    # Permisos: Solo usuarios autenticados pueden modificar/crear; todos pueden leer.
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Sobreescribimos create() para asignar el autor automáticamente
    def perform_create(self, serializer):
        # Asigna el usuario actual como autor del post
        serializer.save(autor=self.request.user)