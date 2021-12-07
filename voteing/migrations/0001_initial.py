# Generated by Django 3.2.9 on 2021-12-03 05:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='add_election',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('electiontype', models.CharField(choices=[('general', 'general'), ('local', 'local')], max_length=100)),
                ('startdate', models.DateField(null=True)),
                ('enddate', models.DateField(null=True)),
                ('electionrules', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='constituency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('constituency', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='leader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leaderName', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='symbol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbolName', models.CharField(choices=[('BALA', 'BALA'), ('LOTA', 'LOTA'), ('SHAR', 'SHAR'), ('TEAR', 'TEAR')], max_length=255)),
                ('symbolImage', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Voters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnic', models.CharField(max_length=200)),
                ('constituency', models.CharField(max_length=200)),
                ('dob', models.DateField()),
                ('image', models.FileField(upload_to='')),
                ('status', models.BooleanField(blank=True, default=False, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seatName', models.CharField(max_length=255)),
                ('constituency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voteing.constituency')),
            ],
        ),
        migrations.CreateModel(
            name='Parties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partyName', models.CharField(choices=[('Pakistan Tehreek-e-Insaf', 'Pakistan Tehreek-e-Insaf'), ('Pakistan Muslim League (N)', 'Pakistan Muslim League (N)'), ('Pakistan Muslim League', 'Pakistan Muslim League'), ('Pakistan Peoples Party', 'Pakistan Peoples Party'), ('Jamaat-e-Islami', 'Jamaat-e-Islami')], max_length=200)),
                ('partyOverview', models.CharField(max_length=255)),
                ('partyLeader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voteing.leader')),
                ('partySymbol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voteing.symbol')),
            ],
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='')),
                ('election', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='voteing.add_election')),
                ('party', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='voteing.parties')),
                ('seat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='voteing.seat')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
