# Generated by Django 4.0.6 on 2022-07-19 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0020_alter_newspage_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='newspage',
            name='publication_date',
            field=models.DateField(auto_now=True, null=True, verbose_name='Publication date'),
        ),
    ]
