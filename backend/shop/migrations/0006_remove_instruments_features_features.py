# Generated by Django 5.1.2 on 2024-11-06 07:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_instruments_features'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instruments',
            name='features',
        ),
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature', models.CharField(blank=True, max_length=255, null=True)),
                ('instrument_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.instruments')),
            ],
        ),
    ]
