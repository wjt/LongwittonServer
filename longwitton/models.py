from django.db import models
from django.contrib import admin

class Game(models.Model):
    STATUS_CHOICES = (
        ( 'noone',  'noone' ),
        ( 'chaser', 'chaser'),
        ( 'chasee', 'chasee'),
    )

    status = models.CharField('game status', choices=STATUS_CHOICES)

    chasee_start_page = models.URLField()
    chaser_start_page = models.URLField()

    chasee_current_page = models.URLField()
    chaser_current_page = models.URLField()

    goal = models.URLField()

    def __unicode__(self):
        return "Game (%s won); goal %s" % (self.status, self.goal)

admin.site.register(Page)
