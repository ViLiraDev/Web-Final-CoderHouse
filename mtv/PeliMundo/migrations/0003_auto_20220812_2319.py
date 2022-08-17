# Generated by Django 3.2.15 on 2022-08-13 02:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PeliMundo', '0002_rename_categoria_pelicula_genero'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pelicula',
            name='genero',
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.CharField(max_length=50)),
                ('pelicula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PeliMundo.pelicula')),
            ],
        ),
    ]