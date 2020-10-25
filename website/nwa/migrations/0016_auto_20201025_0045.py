# Generated by Django 3.1 on 2020-10-25 00:45

from django.db import migrations

def dedup(apps, schema_editor):

    Power = apps.get_model('nwa', 'Power')

    for p in Power.objects.all():
        new_name = p.name + "_tmp"
        if Power.objects.filter(name=new_name, author=p.author).count() == 0:
            newp = Power(name=new_name, author=p.author)
            newp.save()

    copies = list(Power.objects.filter(name__contains='_tmp'))

    to_delete = set()
    for c in copies:
        name = c.name.replace('_tmp', '')
        for p in Power.objects.filter(name=name):
            for e in p.wielded_by.all():
                e.power = c
                e.save()
                to_delete.add(p)

    for p in to_delete:
        p.delete()

    for c in copies:
        name = c.name.replace('_tmp', '')
        c.name = name
        c.save()

    for p in Power.objects.all():
        if not p.wielded_by.count():
            p.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('nwa', '0015_auto_20191125_0122'),
    ]

    operations = [
        migrations.RunPython(dedup),
    ]