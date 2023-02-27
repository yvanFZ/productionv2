# Generated by Django 3.2.15 on 2023-02-20 17:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('is_active', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_loggedin', models.BooleanField(default=False)),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ('date_joined',),
            },
        ),
        migrations.CreateModel(
            name='Functie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('functie', models.CharField(help_text='Enter Functie', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='klantWoningbouw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone_no', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('fax_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('straat', models.CharField(max_length=30)),
                ('postcode', models.CharField(max_length=30)),
                ('provincie', models.CharField(max_length=30)),
                ('land', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.TextField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='MedewerkerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voornaam', models.CharField(max_length=30, verbose_name='voornaam')),
                ('voorletter', models.CharField(max_length=1, null=True)),
                ('tussenvoegsel', models.CharField(max_length=4, null=True)),
                ('achternaam', models.CharField(max_length=30, verbose_name='achternaam')),
                ('geslacht', models.CharField(max_length=30)),
                ('geboortdatum', models.CharField(max_length=30)),
                ('phone_no', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('fax_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('functie', models.ForeignKey(blank=True, default=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.functie')),
                ('rol', models.ForeignKey(blank=True, default=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='role_count', to='users.role')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('voornaam', 'achternaam', 'voorletter'),
            },
        ),
        migrations.AddField(
            model_name='functie',
            name='rol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.role'),
        ),
    ]
