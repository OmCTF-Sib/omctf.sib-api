# Generated by Django 3.2.7 on 2021-09-13 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [  # type: ignore
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Name')),
                ('university', models.CharField(max_length=255, verbose_name='University')),
                ('team_type', models.CharField(max_length=255, verbose_name='Command type')),
                ('score', models.IntegerField(default=0, verbose_name='Score')),
                ('is_visible', models.BooleanField(default=True, verbose_name='Is Visible')),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Teams',
            },
        ),
        migrations.CreateModel(
            name='TeamParticipant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024, verbose_name='Name')),
                ('is_captain', models.BooleanField(default=False, verbose_name='Is Captain')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='teams.team', verbose_name='Team')),
            ],
            options={
                'verbose_name': 'Team participant',
                'verbose_name_plural': 'Team participants',
            },
        ),
    ]
