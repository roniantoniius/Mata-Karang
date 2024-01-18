# admin.py
from django.contrib import admin
from .models import Role, Metode, Pulau, SubmitKarang

admin.site.register(Role)
admin.site.register(Metode)
admin.site.register(Pulau)
admin.site.register(SubmitKarang)