# Generated by Django 3.1.1 on 2023-01-27 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionCouriers', '0012_model_client_apropos'),
    ]

    operations = [
        migrations.AddField(
            model_name='model_client',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='model_client',
            name='telephone',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
