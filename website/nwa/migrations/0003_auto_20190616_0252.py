# Generated by Django 2.2.2 on 2019-06-16 02:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nwa', '0002_auto_20190616_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nwa.Organization'),
        ),
        migrations.AlterField(
            model_name='person',
            name='sector',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nwa.Sector'),
        ),
    ]
