# Generated by Django 4.0.6 on 2022-07-15 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0024_index_image_file_hash'),
        ('profiles', '0016_alter_teampage_created_at_alter_teampage_team_info_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='teampage',
            name='cover',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team_cover', to='wagtailimages.image'),
        ),
    ]
