# Generated by Django 4.2.4 on 2023-08-02 20:00

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('nacionalidad', models.CharField(max_length=30)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('numero_legajo', models.CharField(max_length=30)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('isbn', models.BigIntegerField(validators=[django.core.validators.MinValueValidator(1000000000000), django.core.validators.MaxValueValidator(10000000000000)])),
                ('activo', models.BooleanField(default=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebBiblio.autor')),
            ],
        ),
        migrations.CreateModel(
            name='Socio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='PrestamoLibro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_prestamo', models.DateField()),
                ('fecha_devolucion', models.DateField()),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebBiblio.empleado')),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebBiblio.libro')),
                ('socio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebBiblio.socio')),
            ],
        ),
    ]
