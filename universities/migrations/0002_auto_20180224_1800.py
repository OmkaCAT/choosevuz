# Generated by Django 2.0.2 on 2018-02-24 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialtyscoreforuniversity',
            name='score',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
