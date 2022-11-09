from typing import ByteString
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields.related import ForeignKey


class User(AbstractUser):
    pass

categories= (
    ("Fashion","Fashion"),
    ("Toys","Toys"),
    ("Electronics","Electronics"),
    ("Books","Books"),
)

class Listing(models.Model):
    title = models.CharField(max_length=64 ,primary_key=True)
    discription = models.TextField()
    price = models.IntegerField(default=0)
    current_bid = models.IntegerField(default=0)
    category = models.CharField(choices=categories, default="All", max_length=100, blank=True, null=True)
    imagename = models.CharField(max_length=200, blank = True, null=True)
    imagelink = models.URLField(max_length=250, blank=True, null=True)
    active = models.BooleanField(default=False)
    masteruser = models.CharField(max_length=100, blank=True) 


class Bid(models.Model):
    username = models.CharField(max_length=100)
    bid = models.IntegerField(default=0)
    bids_listing = models.ForeignKey(Listing,on_delete=models.CASCADE, related_name="relate_bid")
    
    
class Comment(models.Model):
    username = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    comment_listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="relate_comments")

class Watchlater(models.Model):
    username = models.CharField(max_length=100)
    watchlater_listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="relate_watchlater")

class Contact_us(models.Model):
    full_name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    message = models.TextField()

    
    
