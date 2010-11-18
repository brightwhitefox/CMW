from django.db import models
from mezzanine.pages.models import Page
#from mezzanine.pages.admin import PageAdmin
from django.contrib import admin
#from mezzanine.core.models import Displayable, Orderable, Content
#from django.utils.translation import ugettext_lazy as _

class News(Page):
    pass

class NewsItem(models.Model):
    #news = models.ForeignKey("News")
    title = models.CharField("Title",editable=True, max_length=100)
    pub_date = models.DateTimeField("Publication Date",help_text="With published selected, won't be shown until this time")
    exp_date = models.DateTimeField("Expiry Date",help_text="With published selected, won't be shown after this time")
    content = models.TextField("Description",editable=True,)
    

    class Admin:
        pass




  
