# Generated by Django 5.0.4 on 2024-04-18 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_identificacion', models.IntegerField(blank=True, null=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='habilitado')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Acceso al admin')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Acceso al admin')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
