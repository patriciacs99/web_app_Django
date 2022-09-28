from django.shortcuts import render
from BlogApp.models import Categoria, Post

# Create your views here.
def blog(request):
    posts = Post.objects.all()
    return render(request,"blog/blog.html",{"posts":posts})

def categoria(request,categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    posts = Post.objects.filter(categoria = categoria)
    return render(request,"blog/categorias.html",{'categoria':categoria,"posts":posts})