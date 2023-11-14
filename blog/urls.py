


from .views import lista_posts, detalle_post, agregar_post, buscar
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('posts/', lista_posts, name='lista_posts'),
    path('post/<int:post_id>/', detalle_post, name='detalle_post'),
    path('agregar_post/', agregar_post, name='agregar_post'),
    path('buscar/', buscar, name='buscar'),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
]


