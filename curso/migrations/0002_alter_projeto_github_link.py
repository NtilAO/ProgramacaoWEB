# Generated by Django 4.0.6 on 2024-04-21 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='github_link',
            field=models.CharField(max_length=200),
        ),
    ]