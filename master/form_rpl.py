from django.forms import ModelForm
from django import forms
from master.models import Siswa

class FormRPL(ModelForm):
    class Meta:
        model = Siswa
        fields = ['NIS', 'nama', 'kelas']

        labels = {
          'NIS':"NIS",
          'nama':'NAMA',
          'kelas':'KELAS',
        }

        widgets = {
            'NIS': forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Masukkan NIS',
                'required': 'required',
                'autofocus': 'autofocus',
                }),
            'nama': forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Masukkan Nama',
                'required': 'required',
                }),
            'kelas': forms.Select(attrs={
                'class': 'form-control selectpicker',
                'data-live-search': 'true',
		'required': 'required',
                }),

        }
