from django.contrib import admin
from .models import *

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']

admin.site.register(Dish)
admin.site.register(Staf)
