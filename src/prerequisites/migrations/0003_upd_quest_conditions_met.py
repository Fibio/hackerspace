# Generated by Django 2.0.13 on 2019-06-11 23:04

from django.db import migrations

from prerequisites.tasks import update_quest_conditions


def forwards(apps, schema_editor):
    update_quest_conditions.apply_async(args=[1], queue='default')


def backwards(apps, schema_editor):
    PrereqAllConditionsMet = apps.get_model("prerequisites", "PrereqAllConditionsMet")
    PrereqAllConditionsMet.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('prerequisites', '0002_prereqallconditionsmet'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]
