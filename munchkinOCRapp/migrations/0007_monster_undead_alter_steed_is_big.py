# Generated by Django 4.2.2 on 2023-06-07 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('munchkinOCRapp', '0006_monstermodifier_description_ru'),
    ]

    operations = [
        migrations.AddField(
            model_name='monster',
            name='undead',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='steed',
            name='is_big',
            field=models.BooleanField(default=True),
        ),
    ]
