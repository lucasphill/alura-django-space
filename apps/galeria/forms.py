from django import forms
from apps.galeria.models import Fotografia

class FotografiaForms(forms.ModelForm):
    class Meta():
        model = Fotografia
        exclude = ['publicada']
        labels = {
            'descricao': 'Descrição',
            'datetime_fotografia': 'Data da fotografia',
            'usuario': 'Fotografo'
        }

        widgets = {
                'nome': forms.TextInput(attrs={'class': 'form-control'}),
                'legenda': forms.TextInput(attrs={'class': 'form-control'}),
                'categoria': forms.Select(attrs={'class': 'form-control'}),
                'descricao': forms.Textarea(attrs={'class': 'form-control'}),
                'foto': forms.FileInput(attrs={'class': 'form-control'}),
                'datetime_fotografia': forms.DateInput(
                    format = '%d/%m/%Y', 
                    attrs = {
                        'class': 'form-control',
                        'type': 'date'
                    }
                ),
                'usuario': forms.Select(attrs={'class': 'form-control'})
        } 