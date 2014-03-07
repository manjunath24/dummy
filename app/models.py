from django.db import models


# Create your models here.
class Institute(models.Model):
    name = models.CharField(max_length=100, verbose_name='Institute Name')
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    contact_person = models.CharField(max_length=100)
    address = models.TextField()
    area = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    #logo = models.ImageField()

    class Meta:
        unique_together = ['name', 'email', 'phone']

    def __unicode__(self):
        return self.name


class Course(models.Model):
    institute = models.ForeignKey(Institute)
    name = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.name
