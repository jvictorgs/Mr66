from django.forms import ModelForm
from app.models import Motos, Compras


# Create the form class.
class MotosForm(ModelForm):
    class Meta:
        model = Motos
        fields = ['modelo', 'marca', 'ano']

class ComprasForm(ModelForm):
    class Meta:
        model = Compras
        fields = ['nome', 'cpf', 'data_nascimento']