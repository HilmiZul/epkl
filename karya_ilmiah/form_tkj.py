from django import forms
from django.forms import ModelForm
from karya_ilmiah.models import KaryaIlmiah

class Form_Karil_TKJ(ModelForm):
    class Meta:
        model = KaryaIlmiah
        fields = ['nama', 'judul', 'tanggal_acc', 'pembimbing']

        labels = {
            'nama': 'NAMA',
            'judul': 'JUDUL',
            'tanggal_acc': 'TANGGAL ACC',
            'pembimbing': 'PEMBIMBING',
        }

        widgets = {
            'nama': forms.Select(attrs={
                'class': 'form-control selectpicker',
                'data-live-search': 'true',
                'required': 'required',
            }),
            'judul': forms.Textarea(attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Tulis judul disini...',
                'required': 'required',
            }),
            'tanggal_acc': forms.TextInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'required': 'required',
            }),
            'pembimbing': forms.Select(attrs={
                'class': 'form-control selectpicker',
                'data-live-search': 'true',
                'required': 'required',
            }),
        }
