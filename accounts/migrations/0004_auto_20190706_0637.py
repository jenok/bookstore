# Generated by Django 2.2.3 on 2019-07-06 06:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190706_0621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 6, 6, 37, 28, 979883, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='account',
            name='text',
            field=models.CharField(max_length=250),
        ),
    ]
