# Generated by Django 2.2.8 on 2020-07-23 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userManager', '0017_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='ticket_type',
            field=models.CharField(choices=[('co', 'course'), ('ge', 'general'), ('su', 'suport')], default=0, max_length=2),
        ),
    ]
