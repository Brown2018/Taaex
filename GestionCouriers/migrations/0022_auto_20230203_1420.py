# Generated by Django 3.1.1 on 2023-02-03 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionCouriers', '0021_model_courrier_traiter'),
    ]

    operations = [
        migrations.AddField(
            model_name='model_courrier',
            name='afecter',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='model_courrier',
            name='consulter',
            field=models.BooleanField(default=False),
        ),
    ]
