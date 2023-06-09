# Generated by Django 3.2.15 on 2023-05-03 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Klant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('klantnaam', models.CharField(default=False, max_length=30)),
                ('plaats', models.CharField(default=False, max_length=30)),
                ('land', models.CharField(default=False, max_length=30)),
                ('provincie', models.CharField(default=False, max_length=30)),
                ('phone', models.CharField(default=False, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='KlantMedewerker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_medewerker', models.CharField(default=False, max_length=30)),
                ('achternaam_medewerker', models.CharField(default=False, max_length=30)),
                ('phone', models.CharField(default=False, max_length=30)),
                ('functie_medewerker', models.CharField(default=False, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Onderaanemerbedrijf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naam', models.CharField(default=False, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectnr', models.CharField(default=False, max_length=30, unique=True)),
                ('projectnaam', models.CharField(default=False, max_length=50)),
                ('plaats', models.CharField(default=False, max_length=15)),
                ('provincie', models.CharField(default=False, max_length=15)),
                ('land', models.CharField(default=False, max_length=15)),
                ('projectStatus', models.CharField(default=False, max_length=15)),
                ('offertenr', models.CharField(blank=True, default=True, max_length=30, null=True)),
                ('exactnr', models.CharField(blank=True, default=True, max_length=30, null=True)),
                ('debiteurnr', models.CharField(blank=True, default=True, max_length=30, null=True)),
                ('renovatie_nieuwbouw', models.CharField(blank=True, default=True, max_length=15, null=True)),
                ('selectedWerkvoorbereiderFz', models.IntegerField(blank=True, default=True, null=True)),
                ('selectedProjecleiderFz', models.IntegerField(blank=True, default=True, null=True)),
                ('inopdrachtvoor_vloerverwarming', models.CharField(blank=True, default=True, max_length=15, null=True)),
                ('inopdrachtvoor_ventilatieinstallatie', models.CharField(blank=True, default=True, max_length=15, null=True)),
                ('inopdrachtvoor_zonnepanelen', models.CharField(blank=True, default=True, max_length=15, null=True)),
                ('datumSystemInvoer', models.CharField(blank=True, default=True, max_length=30, null=True)),
                ('startDatum', models.CharField(blank=True, default=True, max_length=30, null=True)),
                ('offertedatum', models.CharField(blank=True, default=True, max_length=30, null=True)),
                ('uitlijkDatumOpdrachtIndienWTW', models.CharField(blank=True, default=True, max_length=30, null=True)),
                ('uitlijkDatumOpdrachtAlleenICEM', models.CharField(blank=True, default=True, max_length=30, null=True)),
                ('opmerking', models.CharField(blank=True, default=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectIcem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iNumber', models.CharField(default=False, max_length=10)),
                ('pNumber', models.CharField(default=False, max_length=10)),
                ('eNumber', models.CharField(default=False, max_length=10)),
                ('fNumber', models.CharField(default=False, max_length=10)),
                ('aNumber', models.CharField(default=False, max_length=10)),
                ('totaalNumber', models.CharField(default=False, max_length=20)),
                ('estimatedValue', models.CharField(default=False, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='StatusOnderaanemer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default=False, max_length=30)),
                ('odernummer', models.CharField(default=False, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Vertegenwoordiger_Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectnr', models.CharField(default=False, max_length=30)),
            ],
        ),
    ]
