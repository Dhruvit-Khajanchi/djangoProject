# Generated by Django 3.2 on 2021-05-11 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flights',
            name='duration',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
