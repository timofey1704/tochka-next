# Generated by Django 5.1.2 on 2024-11-07 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_remove_texts_artistname_remove_texts_photourl'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstrumentListing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=1000)),
                ('features', models.JSONField()),
                ('images', models.JSONField()),
                ('headertexts', models.JSONField()),
            ],
            options={
                'verbose_name': 'Страница инструменттов',
                'verbose_name_plural': 'Страницы инструментов',
            },
        ),
    ]