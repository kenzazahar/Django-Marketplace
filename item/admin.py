from django.contrib import admin
#try to pull
# Register your models here.

from .models import Category,Item
admin.site.register(Category)
admin.site.register(Item)
