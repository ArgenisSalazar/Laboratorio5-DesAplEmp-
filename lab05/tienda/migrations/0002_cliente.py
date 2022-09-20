# Generated by Django 4.1.1 on 2022-09-20 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=40)),
                ('apellidos', models.CharField(max_length=40)),
                ('dni', models.CharField(max_length=8)),
                ('telefono', models.CharField(max_length=9)),
                ('direccion', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
                ('fecha_publicacion', models.DateField(verbose_name='Fecha de publicacion')),
            ],
        ),
    ]
