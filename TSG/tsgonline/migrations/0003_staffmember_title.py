# Generated by Django 2.0 on 2017-12-11 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tsgonline', '0002_staffmember'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffmember',
            name='title',
            field=models.CharField(default='?', max_length=256),
        ),
    ]