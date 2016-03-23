from django.db import models
from django.utils import timezone

# search term model
class Researcher(models.Model):

    search_term = models.CharField(max_length=200)

    def saveToDB(self):
        self.save()

    def __str__(self):
        return self.search_term

# model for DPLA results
class DplaResult(models.Model):

    url = models.URLField()
    subject_heading1 = models.CharField(max_length=250)
    subject_heading2 = models.CharField(max_length=250)
    subject_heading3 = models.CharField(max_length=250)
    subject_heading4 = models.CharField(max_length=250)
    subject_heading5 = models.CharField(max_length=250)
    subject_heading6 = models.CharField(max_length=250)
    summary = models.CharField(max_length=250)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=250)
    date_published = models.CharField(max_length=250)

# model for images
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

# model for Wikipedia results
class Wiki(models.Model):

    url = models.URLField()
    title = models.CharField(max_length=250)
    summary = models.TextField()



