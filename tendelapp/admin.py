from django.contrib import admin
from django.utils.html import format_html
from .models import Item,Branch,News,Gallery,Team,HomeImage,Modal

# Register your models here.
admin.site.register(Item)
admin.site.register(Branch)
admin.site.register(News)
admin.site.register(Gallery)
admin.site.register(HomeImage)
admin.site.register(Modal)

admin.site.register(Team)

