# Generated by Django 3.2.3 on 2021-06-04 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NCO', '0003_remove_public_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='public',
            name='short_description',
        ),
    ]
