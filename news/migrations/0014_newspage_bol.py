# Generated by Django 4.0.6 on 2022-07-17 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_alter_newscats_bol'),
    ]

    operations = [
        migrations.AddField(
            model_name='newspage',
            name='bol',
            field=models.BooleanField(default=False),
        ),
    ]
