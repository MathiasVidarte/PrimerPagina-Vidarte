

from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'categoria', 'autor']

class BusquedaForm(forms.Form):
    busqueda = forms.CharField(max_length=100, required=False)
