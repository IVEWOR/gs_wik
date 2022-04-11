# Generated by Django 4.0.3 on 2022-04-10 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_setupsettings_related'),
    ]

    operations = [
        migrations.AddField(
            model_name='pcspecs',
            name='section',
            field=models.CharField(choices=[('O', 'Others'), ('GG', 'Gaming Gear'), ('GPS', 'Gaming PC Setup'), ('SPS', 'Streaming PC Setup')], default='O', help_text='GG: Monitor, Mouse, Mousepad, Keyboard, Headset\n        |===| GPS: CPU, GPU, MB, RAM, Case, HDD, SSD, PowerSupply, LCOOL, Fans\n        |===| SPS: Second Mon, ARM, Mic, CAM, WebCam, Chair, Ctrl Panel, AMP,\n        Studio Lit, Light Kit, USB', max_length=3),
        ),
        migrations.AlterField(
            model_name='imagecollection',
            name='alt',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='imagecollection',
            name='caption',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='imagecollection',
            name='title',
            field=models.CharField(max_length=70),
        ),
    ]