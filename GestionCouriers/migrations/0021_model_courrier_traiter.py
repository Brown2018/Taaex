# Generated by Django 3.1.1 on 2023-02-03 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionCouriers', '0020_auto_20230203_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='model_courrier',
            name='traiter',
            field=models.BooleanField(default=False),
        ),
    ]
