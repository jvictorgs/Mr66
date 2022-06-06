from django.forms import ModelForm
from app.models import Motos, Compras, Hist


# Create the form class.
class MotosForm(ModelForm):
    class Meta:
        model = Motos
        fields = ['modelo', 'marca', 'ano']

class ComprasForm(ModelForm):
    class Meta:
        model = Compras
        fields = ['nome', 'cpf', 'data_nascimento']

class HistForm(ModelForm):
    class Meta:
        model = Hist
        fields = ['cpf', 'modelo', 'ano']