# Generated by Django 3.2.9 on 2021-12-15 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voteing', '0020_updates'),
    ]

    operations = [
        migrations.AddField(
            model_name='updates',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]