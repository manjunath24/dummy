from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Institute(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name of Institute')
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50, help_text='Required minimum 6 characters')
    contact_person = models.CharField(max_length=100)
    address = models.TextField()
    area = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    phone = PhoneNumberField()
    is_active = models.BooleanField(default=False)

    class Meta:
        unique_together = ['name', 'email', 'phone']

    def __unicode__(self):
        return self.name


class InstituteActivation(models.Model):
    institute = models.ForeignKey(Institute)
    activation_code = models.CharField(max_length=100)


class Course(models.Model):
    institute = models.ForeignKey(Institute)
    name = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.name
