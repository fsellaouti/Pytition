# Generated by Django 2.2 on 2019-04-17 07:31

from django.db import migrations


def create_slug_through_relations(apps, schema_editor):
    Petition = apps.get_model('petition', 'Petition')
    SlugOwnership = apps.get_model('petition', 'SlugOwnership')
    for petition in Petition.objects.all():
        for slug in petition.slugs.all():
            SlugOwnership(petition=petition, slug=slug).save()


class Migration(migrations.Migration):

    dependencies = [
        ('petition', '0027_slugownership'),
    ]

    operations = [
        migrations.RunPython(create_slug_through_relations, reverse_code=migrations.RunPython.noop),
    ]