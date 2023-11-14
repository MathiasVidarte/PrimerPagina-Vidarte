
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm, BusquedaForm

def lista_posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/lista_posts.html', {'posts': posts})

def detalle_post(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'blog/detalle_post.html', {'post': post})

def agregar_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_posts')
    else:
        form = PostForm()
    return render(request, 'blog/agregar_post.html', {'form': form})

def buscar(request):
    if request.method == 'GET':
        form = BusquedaForm(request.GET)
        if form.is_valid():
            busqueda = form.cleaned_data['busqueda']
            resultados = Post.objects.filter(titulo__icontains=busqueda)
            return render(request, 'blog/resultados_busqueda.html', {'resultados': resultados, 'busqueda': busqueda})
    else:
        form = BusquedaForm()
    return render(request, 'blog/buscar.html', {'form': form})

