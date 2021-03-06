from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=64)
    icon = models.CharField(max_length=32)

    def __unicode__(self):
        return u'(%d) %s' % (self.id, self.name)

class Complaint(models.Model):
    title = models.CharField(max_length=120)
    date = models.DateTimeField()
    reporter = models.ForeignKey(User, related_name='reporter')
    category = models.ForeignKey(Category, related_name='category')

    upvote = models.IntegerField()
    downvote = models.IntegerField()

    latitude = models.DecimalField(max_digits=13, decimal_places=10)
    longtitude = models.DecimalField(max_digits=13, decimal_places=10)

    city = models.CharField(max_length=32)
    address = models.CharField(max_length=120)

    def __unicode__(self):
        return self.title

class Image(models.Model):
    uploader = models.ForeignKey(User)
    complaint = models.ForeignKey(Complaint)
    image = models.TextField()

    def __unicode__(self):
        return '%s (%s)' % (complaint.title, uploader.username)
