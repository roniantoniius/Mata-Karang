from django import forms
from .models import SubmitKarang

class InputKarang(forms.ModelForm):
    class Meta:
        model = SubmitKarang
        fields = '__all__'

        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama Pengguna'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
            'nama_diver': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama Diver'}),
            'waktu_diving': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'pulau': forms.Select(attrs={'class': 'form-control'}),
            'lokasi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Lokasi'}),
            'longittude': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Longitude'}),
            'latittude': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Latitude'}),
            'metode': forms.Select(attrs={'class': 'form-control'}),
            'nama_karang': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama Karang'}),
            'genus_karang': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Genus Karang'}),
            'spesies_karang': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Spesies Karang'}),
            'deskripsi': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Deskripsi'}),
        }
