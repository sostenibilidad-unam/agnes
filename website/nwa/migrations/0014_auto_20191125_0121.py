# Generated by Django 2.2.7 on 2019-11-25 01:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nwa', '0013_auto_20190624_2257'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='mentaledge',
            unique_together={('person', 'source', 'target')},
        ),
    ]