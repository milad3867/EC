# Generated by Django 2.2.8 on 2020-07-22 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userManager', '0004_auto_20200723_0317'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.FileField(null=True, upload_to='profile_pictures/'),
        ),
    ]
