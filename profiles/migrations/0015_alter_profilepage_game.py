# Generated by Django 4.0.6 on 2022-07-14 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0014_gamepage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilepage',
            name='game',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player_game', to='profiles.gamepage'),
        ),
    ]
