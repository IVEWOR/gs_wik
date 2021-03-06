# Generated by Django 4.0.6 on 2022-07-13 12:12

from django.db import migrations, models
import django.utils.timezone
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_profilepage_game_profilepage_is_pro'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilepage',
            name='player_role',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='profilepage',
            name='players_characters',
            field=wagtail.fields.StreamField([('chars', wagtail.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock(required=False)), ('name', wagtail.blocks.CharBlock(required=False))]))], default=django.utils.timezone.now, use_json_field=True),
            preserve_default=False,
        ),
    ]
