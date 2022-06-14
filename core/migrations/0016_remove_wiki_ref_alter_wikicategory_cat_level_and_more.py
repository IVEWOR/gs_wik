# Generated by Django 4.0.4 on 2022-06-13 17:24

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_teamprofile_game_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wiki',
            name='ref',
        ),
        migrations.AlterField(
            model_name='wikicategory',
            name='cat_level',
            field=models.CharField(blank=True, choices=[('r', 'Region'), ('c', 'Country'), ('g', 'Games'), ('t', 'Teams'), ('p', 'Players')], max_length=1, null=True),
        ),
        migrations.CreateModel(
            name='RegionTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('slug', models.SlugField(null=True, unique=True)),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('publish', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('avatar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.imagecollection')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PortalTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('slug', models.SlugField(null=True, unique=True)),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('publish', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('avatar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.imagecollection')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CountryTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('slug', models.SlugField(null=True, unique=True)),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('publish', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('avatar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.imagecollection')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='wiki',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.countrytag'),
        ),
        migrations.AddField(
            model_name='wiki',
            name='portal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.portaltag'),
        ),
        migrations.AddField(
            model_name='wiki',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.regiontag'),
        ),
    ]
