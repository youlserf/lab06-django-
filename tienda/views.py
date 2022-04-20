from django.shortcuts import render, get_object_or_404
from .models import Producto, Categoria
# Create your views here.
def index(request):
    category_list = Categoria.objects.order_by('nombre')[:6]
    product_list = Producto.objects.order_by('nombre')[:6]
    return render(request, 'tienda/index.html', {'product_list': product_list, 'category_list': category_list})

def producto(request, producto_id):
    category_list = Categoria.objects.order_by('nombre')[:6]
    productos = get_object_or_404(Producto, pk=producto_id)
    return render(request, 'tienda/producto.html', {'productos': productos, 'category_list': category_list})

def categoria(request, categoria_id):
    category_list = Categoria.objects.order_by('nombre')[:6]
    categoria =  get_object_or_404(Categoria, pk=categoria_id)
    return render(request, 'tienda/producto.html', {'categoria': categoria, 'category_list': category_list})
