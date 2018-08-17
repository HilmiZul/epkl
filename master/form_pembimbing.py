from django.forms import ModelForm
from django import forms
from master.models import Pembimbing

class FormPembimbing(ModelForm):
    class Meta:
        model = Pembimbing
        fields = ['nama', 'jurusan']

        labels = {
          'nama':"NAMA",
          'jurusan':'JURUSAN',
        }

        widgets = {
            'nama': forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Masukkan Nama',
                'required': 'required',
                }),
            'jurusan': forms.Select(attrs={
                'class': 'form-control selectpicker',
                'data-live-search': 'true',
                'required': 'required',
                }),

        }
