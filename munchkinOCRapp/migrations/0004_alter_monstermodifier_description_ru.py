# Generated by Django 4.2.2 on 2023-06-06 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('munchkinOCRapp', '0003_class_curse_hireling_race_steed_rename_others_misc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monstermodifier',
            name='description_ru',
            field=models.TextField(blank=True, null=True),
        ),
    ]
