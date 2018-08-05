from __future__ import unicode_literals
import os, re, datetime
from django.db import models
from django.contrib.auth.models import User, Group
from django.conf import settings


class CultureAndRecreation(models.Model):
    title = models.CharField(max_length=500)
    release_year = models.IntegerField()
    location = models.CharField(max_length=2000)
    fun_fact = models.TextField()
    production_company = models.CharField(max_length=2000)
    distributor = models.CharField(max_length=1000)
    writer = models.CharField(max_length=500)
    actor1 = models.CharField(max_length=100)
    actor2 = models.CharField(max_length=100)
    actor3 = models.CharField(max_length=100)

    def __str__(self):
        return '{} - {}'.format(self.title, self.release_year)

    def get_dict(self):
        result = {}
        result['title'] = self.title if self.title else None
        result['release_year'] = self.release_year if self.release_year else None
        result['location'] = self.location if self.location else None
        result['fun_fact'] = self.fun_fact if self.fun_fact else None
        result['production_company'] = self.production_company if self.production_company else None
        result['distributor'] = self.distributor if self.distributor else None
        result['writer'] = self.writer if self.writer else None
        result['actor1'] = self.actor1 if self.actor1 else None
        result['actor2'] = self.actor2 if self.actor2 else None
        result['actor3'] = self.actor3 if self.actor3 else None
        return result
