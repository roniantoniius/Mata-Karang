"""tlaut URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from tlaut_apps import views
from tlaut_apps.views import * #* artinya semua diambiil
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("beranda/", beranda),
    path("contact/", contact),
    path("dataai/", dataai),
    path("jawa/", jawa),
    path("kalimantan/", kalimantan),
    path("papua/", papua),
    path("sulawesi/", sulawesi),
    path("sumatera/", sumatera),
    path("datakarang/", datakarang),
    path("submitkarang/", submit_karang),
    path('karang_kelola/', views.karang_kelola, name='karang_kelola'),
    path('karang_edit/<int:id_karang>/', views.karang_edit, name='karang_edit'),
    path('karang_hapus/<int:id_karang>/', views.karang_hapus, name='karang_hapus'),
]+ static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
