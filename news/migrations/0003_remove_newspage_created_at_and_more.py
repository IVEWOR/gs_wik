# Generated by Django 4.0.6 on 2022-07-15 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_newspage_created_at_alter_newspage_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newspage',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='newspage',
            name='updated_at',
        ),
    ]
