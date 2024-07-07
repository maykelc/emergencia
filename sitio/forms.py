from django import forms
from .models import Usuario, Alerta, ubicacion

class LoginForm(forms.Form):
    correo = forms.EmailField(label='Correo Electrónico', required=True)
    contrasena = forms.CharField(label='Contraseña', widget=forms.PasswordInput(), required=True)

class AlertaForm(forms.ModelForm):
    class Meta:
        model = Alerta
        fields = ['titulo', 'descripcion']
        labels = {
            'titulo': 'Título',
            'descripcion': 'Descripción',
        }
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4}),  # Ajustar según tu diseño
        }



class UbicacionForm(forms.ModelForm):
    class Meta:
        model = ubicacion
        fields = ['latitude', 'longitude']