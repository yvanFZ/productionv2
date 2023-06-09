# Generated by Django 3.2.15 on 2023-05-03 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vertegenwoordiger_project',
            name='vertegenwoordiger',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='users.medewerkerprofile'),
        ),
        migrations.AddField(
            model_name='statusonderaanemer',
            name='onderaanemer',
            field=models.ForeignKey(default=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.onderaanemerbedrijf'),
        ),
        migrations.AddField(
            model_name='statusonderaanemer',
            name='project_id',
            field=models.ForeignKey(default=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.project'),
        ),
        migrations.AddField(
            model_name='projecticem',
            name='project',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='project.project'),
        ),
        migrations.AddField(
            model_name='project',
            name='klant',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='project.klant'),
        ),
        migrations.AddField(
            model_name='klantmedewerker',
            name='klant',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='project.klant'),
        ),
        migrations.AddField(
            model_name='klantmedewerker',
            name='project',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='project.project'),
        ),
    ]
