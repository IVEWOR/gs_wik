# Generated by Django 4.0.6 on 2022-07-19 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0022_alter_newspage_publication_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newspage',
            old_name='tags',
            new_name='keywords',
        ),
    ]