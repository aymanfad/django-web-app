# Generated by Django 4.1 on 2022-08-20 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_band_like_new'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='band',
            name='like_new',
        ),
    ]