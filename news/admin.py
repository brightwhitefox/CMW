from django.contrib import admin
from copy import deepcopy
from mezzanine.pages.admin import PageAdmin
from models import News, NewsItem
from mezzanine.core.admin import DisplayableAdmin
from django.db import models

#class NewsitemInline(admin.TabularInline):
#    model = NewsItem

class NewsItemAdmin(admin.ModelAdmin):
    #model = NewsItem
    #inlines = (NewsitemInline,)
    list_display = ("title","pub_date")
    fieldsets = (
        (None, {"fields": ["title",("pub_date" , "exp_date"),"content"]}),
        )
    
admin.site.register(NewsItem,NewsItemAdmin)