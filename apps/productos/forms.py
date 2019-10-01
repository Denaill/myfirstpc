from django import forms 
from apps.productos.models import Producto

class ProductoForm(forms.models.ModelForm):

    class Meta:
        model = Producto

        fields = [
            'nombre',
            'categoria',
            'id_producto',
            'descripcion',
            'valor',
            'plataforma',
            'fecha_publicacion',
        ]

        labels = {
            'nombre': 'Nombre',
            'categoria': 'Categoria',
            'id_producto': 'ID del producto',
            'descripcion': 'Descripcion del producto',
            'valor': 'Costo del producto',
            'plataforma': 'Plataforma en la que se puede instalar',
            'fecha_publicacion': 'Fecha de ingreso a la tienda',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'categoria': forms.TextInput(attrs={'class':'form-control'}),
            'id_producto': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control'}),
            'valor': forms.TextInput(attrs={'class':'form-control'}),
            'plataforma': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_publicacion': forms.DateInput(attrs={'class':'form-control'}),
        }