# Generated by Django 4.1.1 on 2022-09-26 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='contenido',
            field=models.CharField(max_length=1000),
        ),
    ]
