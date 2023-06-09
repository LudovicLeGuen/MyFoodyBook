# Generated by Django 3.2.18 on 2023-05-02 18:49

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=cloudinary.models.CloudinaryField(default='https://www.google.com/url?sa=i&url=https%3A%2F%2Fstock.adobe.com%2Fsearch%3Fk%3Ddefault%2Bavatar&psig=AOvVaw3je7XgNuEkdhlBAActQE2C&ust=1683040511213000&source=images&cd=vfe&ved=0CA4QjRxqFwoTCKi_-NK01P4CFQAAAAAdAAAAABAE', max_length=255, verbose_name='image'),
        ),
    ]
