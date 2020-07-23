# Generated by Django 2.2.8 on 2020-07-23 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userManager', '0016_auto_20200723_2239'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256)),
                ('last_name', models.CharField(blank=True, max_length=256)),
                ('subject', models.CharField(blank=True, max_length=256)),
                ('website', models.CharField(blank=True, max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('text', models.CharField(max_length=256)),
                ('type_of_course', models.IntegerField(choices=[(4, 'momtaz'), (3, 'Awli'), (2, 'khosh'), (1, 'motevaset'), (0, 'test')], default=0)),
            ],
        ),
    ]
