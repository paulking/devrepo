from django.db import models

class Person(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  age = models.IntegerField()
  
  def __unicode__(self):
    return u'%s %s (%d)' % (self.first_name, self.last_name, self.age)