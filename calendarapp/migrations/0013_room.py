# Generated by Django 3.0.8 on 2021-05-24 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendarapp', '0012_auto_20210520_1656'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Room', models.CharField(max_length=200)),
            ],
        ),
    ]
