# Generated by Django 3.2.18 on 2023-04-19 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app_1', '0003_alter_movies_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='image',
            field=models.ImageField(upload_to='dynamic'),
        ),
    ]
