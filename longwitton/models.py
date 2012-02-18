from django.db import models
from django.contrib import admin

class Page(models.Model):
    url = models.URLField()
    timestamp = models.DateTimeField('date visited', auto_now_add=True)

    def __unicode__(self):
        return "%s at %s" % (self.url, self.timestamp.isoformat())

admin.site.register(Page)
