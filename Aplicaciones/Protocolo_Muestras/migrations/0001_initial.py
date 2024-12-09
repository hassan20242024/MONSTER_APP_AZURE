# Generated by Django 4.2 on 2024-11-28 16:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Protocolo_Metodos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViabilidadProceso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_viabilidad', models.CharField(max_length=90, null=True, unique=True, verbose_name='Insumos del Proceso')),
                ('condicion', models.CharField(choices=[('Activo', 'ACTIVO'), ('Pasivo', 'PASIVO')], default='Activo', max_length=90, verbose_name='Condicion')),
            ],
        ),
        migrations.CreateModel(
            name='Proceso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_ingreso', models.DateField(help_text='AAAA/MM/DD', null=True, verbose_name='Fecha de Registro')),
                ('codigo', models.CharField(max_length=90, null=True, unique=True, verbose_name='Código Protocolo')),
                ('nombre', models.CharField(max_length=250, null=True, unique=True, verbose_name='Título_del_Protocolo')),
                ('condicion', models.CharField(choices=[('Activo', 'ACTIVO'), ('Pasivo', 'PASIVO')], default='Activo', max_length=90, verbose_name='Condicion')),
                ('observaciones', models.CharField(max_length=250, null=True, verbose_name='Observaciones')),
                ('fecha_final', models.DateField(blank=True, default=datetime.datetime.now, null=True, verbose_name='Fecha de Finalización')),
                ('Insumos_del_Proceso', models.ManyToManyField(to='Protocolo_Muestras.viabilidadproceso')),
                ('celda', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Protocolo_Metodos.celda', verbose_name='Celda')),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Protocolo_Metodos.cliente', verbose_name='Cliente')),
                ('ensayos', models.ManyToManyField(to='Protocolo_Metodos.ensayo')),
                ('estado_del_proceso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Protocolo_Metodos.estadoprotocolo', verbose_name='Estado del proceso')),
                ('metodo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Protocolo_Metodos.metodo', verbose_name='Metodo de referencia')),
                ('metodologia', models.ForeignKey(max_length=90, null=True, on_delete=django.db.models.deletion.CASCADE, to='Protocolo_Metodos.metodologia', verbose_name='metodologia')),
                ('muestras', models.ManyToManyField(to='Protocolo_Metodos.muestras_y_placebos')),
            ],
        ),
    ]
