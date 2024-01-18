from django.db import models

class Role(models.Model):
    id_role = models.AutoField(primary_key=True)
    role = models.CharField(max_length=255)

    def __str__(self):
        return self.role

class Metode(models.Model):
    id_metode = models.AutoField(primary_key=True)
    metode_data = models.CharField(max_length=255)

    def __str__(self):
        return self.metode_data

class Pulau(models.Model):
    id_pulau = models.AutoField(primary_key=True)
    nama_pulau = models.CharField(max_length=255)

    def __str__(self):
        return self.nama_pulau
    

class SubmitKarang(models.Model):
    id_karang = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=255)
    email = models.EmailField()
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    nama_diver = models.CharField(max_length=255)
    waktu_diving = models.DateField()
    pulau = models.ForeignKey(Pulau, on_delete=models.CASCADE)
    lokasi = models.CharField(max_length=255)
    longittude = models.CharField(max_length=255)
    latittude = models.CharField(max_length=255)
    metode = models.ForeignKey(Metode, on_delete=models.CASCADE)
    nama_karang = models.CharField(max_length=255)
    genus_karang = models.CharField(max_length=255)
    spesies_karang = models.CharField(max_length=255)
    deskripsi = models.TextField()
    gambar = models.ImageField(null=True, blank=True, upload_to="media/")

    def __str__(self):
        return f"{self.nama} - {self.nama_karang}"


