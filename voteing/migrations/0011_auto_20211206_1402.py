# Generated by Django 3.2.9 on 2021-12-06 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voteing', '0010_auto_20211206_1357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='election',
        ),
        migrations.AddField(
            model_name='candidate',
            name='election',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='voteing.add_election'),
        ),
    ]
