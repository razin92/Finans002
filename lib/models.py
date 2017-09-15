from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    firstname = models.CharField(max_length=20)
    secondname = models.CharField(max_length=20, verbose_name=(u'Фамилия'), blank=True)

    def __str__(self):
        return self.firstname + ' ' + self.secondname

    class Meta():
        unique_together = ('firstname', 'secondname')


class Pouch(models.Model):
    name = models.CharField(max_length=20, unique=True)
    value = (
        (u'SUM', u'SUM'),
        (u'$', u'USD')
    )
    balance = models.IntegerField(verbose_name=(u'Balance'), default=0, blank=False)
    starting_balance = models.IntegerField(verbose_name=(u'Начальный баланс'), default=0)
    type = models.CharField(max_length=3, choices=value, default='(SUM)')
    comment = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Staff(models.Model):
    name = models.OneToOneField(User)
    pouches = models.ManyToManyField(Pouch)
    telephone = models.BigIntegerField(null=True, blank=True, unique=True)

    def __str__(self):
        return str(self.name.username)