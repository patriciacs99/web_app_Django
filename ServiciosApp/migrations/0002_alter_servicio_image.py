# Generated by Django 4.1.1 on 2022-09-26 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ServiciosApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='image',
            field=models.ImageField(upload_to='servicios'),
        ),
    ]
