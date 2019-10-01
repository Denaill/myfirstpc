from django.shortcuts import render, redirect
from django.http  import HttpResponse
from apps.productos.forms import ProductoForm
from apps.productos.models import Producto
from django.views.generic import ListView

# Create your views here.

def index(request):
    return render(request, 'productos/index.html')

def producto_view(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form =ProductoForm()

    return render(request, 'productos/producto_form.html', {'form':form})

class ProductoList(ListView):
    model = Producto
    template_name = "productos/producto_list.html"
    paginate_by = 4

def producto_edit(request, id_producto):
    producto = Producto.objects.get(id=id_producto)
    if request.method == 'GET':
        form = ProductoForm(instance=producto)
    else:
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
        return redirect('producto_listar')
    return render(request, 'productos/producto_edit.html', {'form':form})

def producto_delete(request, id_producto):
    producto = Producto.objects.get(id=id_producto)
    if request.method == 'POST':
        producto.delete()
        return redirect('producto_listar')
    return render(request, 'productos/producto_delete.html', {'producto':producto})