from django.contrib import admin

# Register your models here.

from .models import Listing, Bid, Comment, User, Watchlater, Contact_us

admin.site.register(User)
admin.site.register(Listing)
admin.site.register(Bid)
admin.site.register(Comment)
admin.site.register(Watchlater)
admin.site.register(Contact_us)