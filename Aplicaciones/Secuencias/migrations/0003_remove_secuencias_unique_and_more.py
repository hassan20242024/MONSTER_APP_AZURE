# Generated by Django 4.2.7 on 2024-12-20 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Secuencias", "0002_remove_secuencias_unique_and_more"),
    ]

    operations = [
        migrations.RemoveConstraint(model_name="secuencias", name="unique",),
        migrations.RemoveConstraint(model_name="secuencias", name="unique_intro_nue",),
        migrations.AddConstraint(
            model_name="secuencias",
            constraint=models.UniqueConstraint(
                fields=("protocolo", "parametro_sq", "fecha_invalidar"), name="unique"
            ),
        ),
        migrations.AddConstraint(
            model_name="secuencias",
            constraint=models.UniqueConstraint(
                fields=("protocolo_proceso", "muestras", "fecha_invalidar"),
                name="unique_intro_nue",
            ),
        ),
    ]
