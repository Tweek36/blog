# Generated by Django 4.1.7 on 2023-04-26 23:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_blog_posted_coment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2023, 4, 27, 2, 23, 24, 557450)),
        ),
        migrations.AlterField(
            model_name='coment',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2023, 4, 27, 2, 23, 24, 557450)),
        ),
    ]