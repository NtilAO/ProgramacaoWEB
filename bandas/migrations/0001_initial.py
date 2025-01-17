# Generated by Django 4.0.6 on 2024-04-16 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tituloAlbum', models.CharField(max_length=100)),
                ('anoDeLancamento', models.IntegerField()),
                ('capa', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Banda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Musica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tituloMusica', models.CharField(max_length=100)),
                ('anoDeLancamento', models.IntegerField()),
                ('link', models.URLField()),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bandas.album')),
                ('banda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bandas.banda')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='banda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bandas.banda'),
        ),
    ]
