# Generated by Django 3.1.7 on 2021-05-25 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_auto_20210525_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='upload',
        ),
    ]
