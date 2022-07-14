# Generated by Django 4.0.6 on 2022-07-14 10:05

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0024_index_image_file_hash'),
        ('wagtailcore', '0069_log_entry_jsonfield'),
        ('profiles', '0013_remove_country_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='GamePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('created_at', models.DateTimeField(null=True, verbose_name='Post date')),
                ('updated_at', models.DateTimeField(null=True, verbose_name='Last updated')),
                ('full_name', models.CharField(blank=True, max_length=100)),
                ('intro', wagtail.fields.RichTextField(blank=True, null=True)),
                ('body', wagtail.fields.RichTextField(blank=True, null=True)),
                ('avatar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='game_avatar', to='wagtailimages.image')),
                ('cover', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='game_cover', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]