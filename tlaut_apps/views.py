from django.shortcuts import render, redirect, HttpResponse
import uuid
from .forms import *
from django.conf import settings
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def beranda(request):
        return render(request, "beranda.html")

def datakarang(request):
        return render(request, "datakarang.html")

def contact(request):
        return render(request, "contact.html")

def dataai(request):
        return render(request, "dataai.html")

def jawa(request):
        karangs = SubmitKarang.objects.all()
        return render(request, 'jawa.html', {'karangs': karangs})

def kalimantan(request):
        karangs = SubmitKarang.objects.all()
        return render(request, 'kalimantan.html', {'karangs': karangs})

def papua(request):
        karangs = SubmitKarang.objects.all()
        return render(request, 'papua.html', {'karangs': karangs})

def sulawesi(request):
        karangs = SubmitKarang.objects.all()
        return render(request, 'sulawesi.html', {'karangs': karangs})

def sumatera(request):
        karangs = SubmitKarang.objects.all()
        return render(request, 'sumatera.html', {'karangs': karangs})


def submit_karang(request):
    if request.method == 'POST':
        form = InputKarang(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/beranda')  # Ganti dengan URL yang sesuai setelah berhasil submit
    else:
        form = InputKarang()

    context = {
        'form': form,
    }
    return render(request, 'submitKarang.html', context)

def karang_kelola(request):
    karangs = SubmitKarang.objects.all()
    return render(request, 'karangKelola.html', {'karangs': karangs})

def karang_edit(request, id_karang):
    karang = SubmitKarang.objects.get(id=id_karang)

    if request.method == 'POST':
        form = InputKarang(request.POST, instance=karang)
        if form.is_valid():
            form.save()
            return redirect('karang_kelola')
    else:
        form = InputKarang(instance=karang)

    return render(request, 'karangEdit.html', {'form': form, 'karang': karang})

def karang_hapus(request, id_karang):
    karang = SubmitKarang.objects.get(id=id_karang)
    karang.delete()
    return redirect('karang_kelola')