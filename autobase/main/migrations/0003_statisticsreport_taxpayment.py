# Generated by Django 5.0.6 on 2024-05-19 10:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_request_request_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatisticsReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_date', models.DateField()),
                ('report_file', models.FileField(upload_to='reports/')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.request')),
            ],
        ),
        migrations.CreateModel(
            name='TaxPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_date', models.DateField()),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.request')),
            ],
        ),
    ]
