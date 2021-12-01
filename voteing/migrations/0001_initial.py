# Generated by Django 3.2.9 on 2021-11-26 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party_Name', models.CharField(max_length=200)),
                ('party_Leader', models.CharField(max_length=200)),
                ('party_Symbol', models.CharField(max_length=200)),
                ('party_Overview', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_Name', models.CharField(max_length=255)),
            ],
        ),
    ]
