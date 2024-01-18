# Generated by Django 4.1.3 on 2023-12-18 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Metode",
            fields=[
                ("id_metode", models.AutoField(primary_key=True, serialize=False)),
                ("metode_data", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Pulau",
            fields=[
                ("id_pulau", models.AutoField(primary_key=True, serialize=False)),
                ("nama_pulau", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Role",
            fields=[
                ("id_role", models.AutoField(primary_key=True, serialize=False)),
                ("role", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="SubmitKarang",
            fields=[
                ("id_karang", models.AutoField(primary_key=True, serialize=False)),
                ("nama", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                ("nama_diver", models.CharField(max_length=255)),
                ("waktu_diving", models.DateField()),
                ("lokasi", models.CharField(max_length=255)),
                ("longittude", models.CharField(max_length=255)),
                ("latittude", models.CharField(max_length=255)),
                ("nama_karang", models.CharField(max_length=255)),
                ("genus_karang", models.CharField(max_length=255)),
                ("spesies_karang", models.CharField(max_length=255)),
                ("deskripsi", models.TextField()),
                (
                    "metode",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tlaut_apps.metode",
                    ),
                ),
                (
                    "pulau",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tlaut_apps.pulau",
                    ),
                ),
                (
                    "role",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tlaut_apps.role",
                    ),
                ),
            ],
        ),
    ]