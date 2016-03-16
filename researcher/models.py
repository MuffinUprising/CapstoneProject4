from django.db import models
from django.utils import timezone

class Search(models.Model):

    search_term = models.CharField(max_length=200)

    def saveToDB(self):
        self.save()

    def __str__(self):
        return self.search_term


