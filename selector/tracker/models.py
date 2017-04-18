from django.db import models

from django.dispatch import receiver
from django.db.models.signals import post_save

from django.contrib.auth.models import User

from django.db.models.aggregates import Count
from random import randint

# Create your models here.


class Account(models.Model):

    user = models.OneToOneField('auth.User')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender='auth.User')
def create_user_profile(**kwargs):
    created = kwargs.get('created')
    instance = kwargs.get('instance')
    if created:
        Account.objects.create(user=instance)


class List(models.Model):

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User)

    def __str__(self):
        return str(self.name)


class RandomOptionManager(models.Manager):
    def random(self):
        count = self.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        return self.all()[random_index]
    # def get_queryset(self):
    #     return super(RandomOptionManager, self).get_queryset().filter(author='Roald Dahl')


class Option(models.Model):

    name = models.CharField(max_length=30)
    details = models.CharField(max_length=108, null=True, blank=True)
    related_list = models.ForeignKey(List)

    def __str__(self):
        return str(self.name)
