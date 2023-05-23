from django.contrib import admin
from django.utils.html import format_html
from .models import Item,IpModel,Branch,News,Gallery,Offer,Team

# Register your models here.
admin.site.register(Item)
admin.site.register(Branch)
admin.site.register(News)
admin.site.register(Gallery)
admin.site.register(Offer)
admin.site.register(Team)
admin.site.register(IpModel)
