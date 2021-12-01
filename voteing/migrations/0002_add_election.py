# Generated by Django 3.2.9 on 2021-11-26 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voteing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_election',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('election_type', models.CharField(max_length=100)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('election_rules', models.CharField(max_length=255)),
            ],
        ),
    ]