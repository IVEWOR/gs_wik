# Generated by Django 4.0.4 on 2022-05-25 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_remove_news_tags_news_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='news_tags', to='core.newscategory'),
        ),
    ]
