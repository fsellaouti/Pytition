# Generated by Django 2.2 on 2019-04-19 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('petition', '0036_organization_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petition',
            name='org',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='petition.Organization'),
        ),
        migrations.AlterField(
            model_name='petition',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='petition.PytitionUser'),
        ),
        migrations.AlterField(
            model_name='petitiontemplate',
            name='org',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='petition.Organization'),
        ),
        migrations.AlterField(
            model_name='petitiontemplate',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='petition.PytitionUser'),
        ),
    ]
