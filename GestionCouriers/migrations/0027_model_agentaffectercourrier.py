# Generated by Django 3.1.1 on 2023-02-04 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datacenter', '0019_model_moi'),
        ('GestionCouriers', '0026_auto_20230203_2337'),
    ]

    operations = [
        migrations.CreateModel(
            name='Model_AgentAffecterCourrier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_ent', models.CharField(blank=True, max_length=150, null=True)),
                ('codex', models.CharField(blank=True, max_length=120, null=True, unique=True)),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agent_courrier', to='datacenter.model_utilisateur')),
                ('courrier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='courrier', to='GestionCouriers.model_courrier')),
                ('entreprise', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='affectercourrier_entreprise', to='datacenter.entreprise')),
            ],
        ),
    ]
