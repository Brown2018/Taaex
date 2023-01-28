# Generated by Django 3.1.1 on 2023-01-24 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datacenter', '0012_auto_20211003_1520'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('titre', models.CharField(blank=True, max_length=100, null=True)),
                ('icon', models.CharField(blank=True, max_length=100, null=True)),
                ('background_color', models.CharField(blank=True, max_length=100, null=True)),
                ('background_image', models.CharField(blank=True, max_length=100, null=True)),
                ('url', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Entreprise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intitule', models.CharField(blank=True, max_length=50, null=True)),
                ('Forme_juridique', models.CharField(blank=True, max_length=50, null=True)),
                ('rccm', models.CharField(blank=True, max_length=50, null=True)),
                ('siren', models.CharField(blank=True, max_length=150, null=True)),
                ('Date_creation_entreprise', models.DateField(blank=True, null=True)),
                ('Effectifs', models.CharField(blank=True, max_length=50, null=True)),
                ('code', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='paiement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('app', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='app_paie', to='datacenter.apps')),
                ('entreprise', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entreprise_paie', to='datacenter.entreprise')),
            ],
        ),
        migrations.CreateModel(
            name='entrepriseApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etat', models.BooleanField(blank=True, default=False, null=True)),
                ('app', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='app_r', to='datacenter.apps')),
                ('entreprise', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entrepriseApp', to='datacenter.entreprise')),
            ],
        ),
        migrations.AddField(
            model_name='model_utilisateur',
            name='entreprise',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mon_entreprise', to='datacenter.entreprise'),
        ),
    ]
