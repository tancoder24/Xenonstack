# Generated by Django 3.1.7 on 2021-05-26 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_auto_20210526_1951'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='masteruser',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='bid',
            name='bids_listing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relate_bid', to='auctions.listing'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='auction_Listing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relate_comments', to='auctions.listing'),
        ),
    ]