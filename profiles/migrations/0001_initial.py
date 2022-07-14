# Generated by Django 4.0.6 on 2022-07-12 17:02

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0069_log_entry_jsonfield'),
        ('wagtailimages', '0024_index_image_file_hash'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('name', models.CharField(max_length=255)),
                ('iso', models.CharField(max_length=2)),
                ('flag', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='flag_image', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ProfileIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro', wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ProfilePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('created_at', models.DateTimeField(verbose_name='Post date')),
                ('updated_at', models.DateTimeField(null=True, verbose_name='Last updated')),
                ('full_name', models.CharField(blank=True, max_length=150)),
                ('native_name', models.CharField(blank=True, max_length=150)),
                ('intro', models.CharField(max_length=250)),
                ('hometown', models.CharField(blank=True, max_length=150)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('body', wagtail.fields.RichTextField(blank=True)),
                ('avatar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='profile_avatar', to='wagtailimages.image')),
                ('player_country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='profile_country', to='profiles.country')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='Specs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('product_type', models.CharField(blank=True, choices=[('CPU', 'CPU'), ('GPU', 'GPU'), ('RAM', 'RAM'), ('SSD', 'SSD'), ('CASE', 'Case'), ('MB', 'Motherboard'), ('PS', 'Power Supply'), ('HDD', 'Hard Drive'), ('KBD', 'Keyboard'), ('MOU', 'Mouse'), ('MON', 'Monitor'), ('CAM', 'Camera'), ('WEB', 'WEBCAM'), ('SPE', 'Speaker'), ('ARM', 'ARM'), ('MIC', 'Microphone'), ('MP', 'Mousepad'), ('HS', 'Headset'), ('CHAIR', 'Chair'), ('LC', 'Liquid Cooling')], max_length=150)),
                ('product_name', models.CharField(blank=True, max_length=150, null=True)),
                ('amazon_url', models.URLField(blank=True, null=True)),
                ('product_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='spec_image', to='wagtailimages.image')),
                ('profile', modelcluster.fields.ParentalKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player_specs', to='profiles.profilepage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SettingsMain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('title', models.CharField(max_length=150)),
                ('profile_settings', wagtail.fields.StreamField([('section_settings', wagtail.blocks.StructBlock([('sub_heading', wagtail.blocks.CharBlock(required=False)), ('section_details', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('key_name', wagtail.blocks.CharBlock(required=False)), ('value_name', wagtail.blocks.CharBlock(required=False))])))]))], use_json_field=True)),
                ('profile', modelcluster.fields.ParentalKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player_settings', to='profiles.profilepage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]