# Generated by Django 4.0.6 on 2022-09-08 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('account_id', models.AutoField(primary_key=True, serialize=False)),
                ('balance', models.IntegerField()),
                ('iban', models.TextField()),
                ('account_type', models.TextField(blank=True, null=True)),
                ('customer_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cuenta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('loan_id', models.AutoField(primary_key=True, serialize=False)),
                ('loan_type', models.TextField()),
                ('loan_date', models.TextField()),
                ('loan_total', models.IntegerField()),
                ('customer_id', models.IntegerField(blank=True, null=True)),
                ('branch_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'prestamo',
                'managed': False,
            },
        ),
    ]