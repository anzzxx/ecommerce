# Generated by Django 5.0.6 on 2024-09-05 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('variation', '0002_variation_is_default'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variation',
            name='is_default',
        ),
    ]
