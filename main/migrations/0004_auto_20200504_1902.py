# Generated by Django 3.0.3 on 2020-05-04 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200226_2015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='owner_id',
            new_name='owner',
        ),
    ]