from django import forms
from .models import Task
from datetime import datetime

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'due_date']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'text', 'placeholder': 'DD/MM/AAAA'}),
        }

def clean_due_date(self):
    data = self.cleaned_data['due_date']
    try:
        # Converte o formato brasileiro (DD/MM/AAAA) para o formato ISO (YYYY-MM-DD)
        data_formatada = datetime.strptime(data, '%d/%m/%Y').date()
    except ValueError:
        raise forms.ValidationError('Insira a data no formato DD/MM/AAAA')
    return data_formatada
