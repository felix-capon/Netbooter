# Generated by Django 4.1.1 on 2022-09-14 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('httpserver', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='version',
            new_name='name',
        ),
    ]