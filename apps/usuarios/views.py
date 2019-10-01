from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy
from apps.usuarios.forms import RegistroForm
from apps.usuarios.models import Usuarios

class RegistroUsuario(CreateView):
    model = User
    template_name = "usuarios/usuario_form.html"
    form_class = RegistroForm
    success_url = reverse_lazy('index')

class UsuarioList(ListView):
    model = User
    template_name = "usuarios/usuario_list.html"
    paginate_by = 4

def usuario_edit(request, id_usuario):
    usuario = User.objects.get(id=id_usuario)
    if request.method == 'GET':
        form = RegistroForm(instance=usuario)
    else:
        form = RegistroForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
        return redirect('usuario_listar')
    return render(request, 'usuarios/usuario_edit.html', {'form':form})

def usuario_delete(request, id_usuario):
    usuario = User.objects.get(id=id_usuario)
    if request.method == 'POST':
        usuario.delete()
        return redirect('usuario_listar')
    return render(request, 'usuarios/usuario_delete.html', {'usuario':usuario})

