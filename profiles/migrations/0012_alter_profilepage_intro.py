# Generated by Django 4.0.6 on 2022-07-13 18:18

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0011_alter_teampage_intro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilepage',
            name='intro',
            field=wagtail.fields.RichTextField(blank=True, null=True),
        ),
    ]
