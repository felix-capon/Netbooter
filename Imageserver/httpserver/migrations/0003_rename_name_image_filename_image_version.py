# Generated by Django 4.1.1 on 2022-09-14 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('httpserver', '0002_rename_version_image_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='name',
            new_name='filename',
        ),
        migrations.AddField(
            model_name='image',
            name='version',
            field=models.CharField(default='V3', max_length=200),
            preserve_default=False,
        ),
    ]
