from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from administrativo.models import Edificio, \
        Departamento

class EdificioForm(ModelForm):
    class Meta:
        model = Edificio
        fields = ['nombre', 'direccion', 'ciudad', 'tipo']
        labels = {
            'nombre': _('Ingrese nombre por favor'),
            'direccion': _('Ingrese la direccion por favor'),
            'ciudad': _('Ingrese la ciudad por favor'),
            'tipo': _('Ingrese el tipo por favor'),
        }

    def clean_ciudad(self):
        valor = self.cleaned_data['ciudad']
        if valor.split()[0][0] == "L":
            raise forms.ValidationError("Ingrese ciudad diferente a la primera  letra con L")
        return valor



class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['propietario', 'costoDep', 'numCuartos',  'edificio']
        labels = {
            'propietario': _('Ingrese nombre de el propietario'),
            'costoDep': _('Ingrese el costo del departamento'),
            'numCuartos': _('Ingrese el numero de cuartos'),
            'edificio': _('Escoga el edificio'),
        }
    
    def clean_costoDep(self):
        valor = self.cleaned_data['costoDep']
        if float(valor) > 100000:
            raise forms.ValidationError("Ingrese un numero menor a 100k")
        return valor
    
    def clean_numCuartos(self):
        valor = self.cleaned_data['numCuartos']
        if int(valor) <= 0 or int(valor) > 7:
            raise forms.ValidationError("Ingrese valor distitno a 0 o menor a 7")
        return valor
    
    def clean_propietario(self):
        valor = self.cleaned_data['propietario']
        if len(valor.split()) <= 3:
            raise forms.ValidationError("Ingrese mas de 3 nombres")
        return valor

class DepartamentoEdificioForm(ModelForm):

    def __init__(self, departamento, *args, **kwargs):
        super(DepartamentoEdificioForm, self).__init__(*args, **kwargs)
        self.initial['departamento'] = edificio
        self.fields["departamento"].widget = forms.widgets.HiddenInput()
        print(edificio)

    class Meta:
        model = Departamento
        fields = ['propietario', 'costoDep', 'numCuartos',  'edificio']

class DepartamentoEdificioForm(ModelForm):

    def __init__(self, edificio, *args, **kwargs):
        super(DepartamentoEdificioForm, self).__init__(*args, **kwargs)
        self.initial['edificio'] = edificio
        self.fields["edificio"].widget = forms.widgets.HiddenInput()
        print(edificio)

    class Meta:
        model = Departamento
        fields = ['propietario', 'costoDep', 'numCuartos',  'edificio']
