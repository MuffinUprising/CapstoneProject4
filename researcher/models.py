from django.db import models
from django.utils import timezone


class Search(models.Model):

    search_term = models.CharField(max_length=200)

    def saveToDB(self):
        self.save()

    def __str__(self):
        return self.search_term


class DplaResult(models.Model):

    url = models.URLField()
    subject_heading1 = models.CharField(max_length=250)
    subject_heading2 = models.CharField(max_length=250)
    subject_heading3 = models.CharField(max_length=250)
    summary = models.CharField(max_length=250)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=250)
    date_published = models.CharField(max_length=250)

    def buildSHList(self, subject_heading1, subject_heading2, subject_heading3):
        subject_headings = []
        subject_headings.append(subject_heading1)
        subject_headings.append(subject_heading2)
        subject_headings.append(subject_heading3)



class Images(models.Model):

    imageURL1 = models.URLField()
    imageURL2 = models.URLField()
    imageURL3 = models.URLField()
    imageURL4 = models.URLField()
    imageURL5 = models.URLField()

    def buildImageList(self, imageURL1, imageURL2, imageURL3, imageURL4, imageURL5):
        imageList = []
        imageList.append(imageURL1)
        imageList.append(imageURL2)
        imageList.append(imageURL3)
        imageList.append(imageURL4)
        imageList.append(imageURL5)



class Wiki(models.Model):

    url = models.URLField()
    title = models.CharField(max_length=250)
    summary = models.TextField()


