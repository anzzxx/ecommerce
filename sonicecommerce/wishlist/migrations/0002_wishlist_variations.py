# Generated by Django 5.0.6 on 2024-09-10 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('variation', '0004_variation_defult'),
        ('wishlist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='variations',
            field=models.ManyToManyField(blank=True, to='variation.variation'),
        ),
    ]
