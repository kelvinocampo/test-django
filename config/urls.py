# mysite/urls.py (o config/urls.py)

from django.contrib import admin
from django.urls import path, include
from users.views import UserDetailView, UserUpdateView, RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
    path('register/', RegisterView.as_view(), name='register'),
    path('', include('django.contrib.auth.urls')),
    path('profile/<str:username>/', UserDetailView.as_view(), name='user_detail'),
    path('profile/<str:username>/edit/', UserUpdateView.as_view(), name='user_update'),
]