# Generated by Django 2.2.10 on 2020-03-19 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Signing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=140, null=True, verbose_name='Nombre completo')),
                ('original_string', models.TextField(blank=True, null=True, verbose_name='Cadena original')),
                ('invoice', models.CharField(blank=True, max_length=150, null=True, verbose_name='Folio de consulta')),
                ('signing_type', models.CharField(blank=True, max_length=50, null=True, verbose_name='Tipo de firma')),
                ('user', models.CharField(blank=True, max_length=80, null=True, verbose_name='Usuario verificado')),
                ('curp', models.CharField(blank=True, max_length=18, null=True, verbose_name='CURP')),
                ('rfc', models.CharField(blank=True, max_length=13, null=True, verbose_name='R.F.C.')),
                ('query_sat', models.CharField(blank=True, max_length=20, null=True, verbose_name='Consulta SAT')),
                ('status_cert', models.CharField(blank=True, max_length=50, null=True, verbose_name='Estatus certificado')),
                ('stamp', models.TextField(blank=True, null=True, verbose_name='Sello')),
                ('active', models.BooleanField(default=True, verbose_name='Activo')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'firma',
                'verbose_name_plural': 'firmas',
            },
        ),
    ]