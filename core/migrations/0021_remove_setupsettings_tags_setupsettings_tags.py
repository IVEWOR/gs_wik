# Generated by Django 4.0.4 on 2022-06-03 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_setupsettings_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setupsettings',
            name='tags',
        ),
        migrations.AddField(
            model_name='setupsettings',
            name='tags',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='setup_tags', to='core.wikicategory'),
        ),
    ]