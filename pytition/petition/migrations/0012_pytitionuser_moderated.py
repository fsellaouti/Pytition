# Generated by Django 2.2.16 on 2021-06-03 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petition', '0011_auto_20210524_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='pytitionuser',
            name='moderated',
            field=models.BooleanField(default=False),
        ),
    ]