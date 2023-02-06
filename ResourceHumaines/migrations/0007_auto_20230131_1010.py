# Generated by Django 3.1.1 on 2023-01-31 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ResourceHumaines', '0006_auto_20230130_1452'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='model_employer',
            name='fonction',
        ),
        migrations.RemoveField(
            model_name='model_employer',
            name='poste',
        ),
        migrations.CreateModel(
            name='Model_Employer_Fonction_Poste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_engagement', models.DateField(blank=True, null=True)),
                ('employer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employer_fonction_poste', to='ResourceHumaines.model_employer')),
                ('fonction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mon_fonction', to='ResourceHumaines.model_employer_fonction')),
                ('poste', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mon_poste', to='ResourceHumaines.model_postes_fonction')),
            ],
        ),
    ]
