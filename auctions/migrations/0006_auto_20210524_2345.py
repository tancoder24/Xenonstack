# Generated by Django 3.1.7 on 2021-05-24 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20210524_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='title',
            field=models.CharField(help_text='enter title', max_length=64, primary_key=True, serialize=False),
        ),
    ]
