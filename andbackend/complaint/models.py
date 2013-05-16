from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=64)
    icon = models.ImageField(upload_to='/srv/android/andbackend/static/icons')

    def __unicode__(self):
        return u'(%d) %s' % (self.id, self.name)

class Complaint(models.Model):
    title = models.CharField(max_length=120)
    date = models.DateField()
    reporter = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    image = models.ImageField(upload_to='/srv/android/andbackend/static/img')

    upvote = models.IntegerField()
    downvote = models.IntegerField()

    latitude = models.DecimalField(max_digits=13, decimal_places=10)
    longtitude = models.DecimalField(max_digits=13, decimal_places=10)

    city = models.CharField(max_length=32)
    address = models.CharField(max_length=120)

    def __unicode__(self):
        return self.title

    def pre_save(self, obj):
        obj.reporter = self.request.user
