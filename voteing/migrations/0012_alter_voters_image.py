# Generated by Django 3.2.9 on 2021-12-06 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voteing', '0011_auto_20211206_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voters',
            name='image',
            field=models.FileField(upload_to='voter/'),
        ),
    ]