# Generated by Django 3.1.4 on 2021-03-23 17:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('security', '0002_model_utilisateur_esclave'),
    ]

    operations = [
        migrations.AddField(
            model_name='model_utilisateur_esclave',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='utilisateur_esclave_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
