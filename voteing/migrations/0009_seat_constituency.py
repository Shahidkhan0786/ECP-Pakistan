# Generated by Django 3.2.9 on 2021-11-27 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voteing', '0008_constituency'),
    ]

    operations = [
        migrations.AddField(
            model_name='seat',
            name='constituency',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='voteing.constituency'),
            preserve_default=False,
        ),
    ]
