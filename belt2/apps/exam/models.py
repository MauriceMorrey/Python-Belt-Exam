# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login_and_registration.models import User

# Create your models here.
class WishManager(models.Manager):
    def wish_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors['name'] = 'Item name should be more than 3 characters'
        if len(postData["name"])==0:
            errors["name"] = "Item name cannot be empty!"
        return errors

class Wish(models.Model):
    name = models.CharField(max_length=255)
    creator = models.ForeignKey(User, related_name='Items_created')
    date_added = models.DateField(auto_now_add=True)   
    wishers = models.ManyToManyField(User, related_name='Items_wished')
    objects = WishManager()

    def __str__(self):
        return self.name

    # def __repr__(self):
    #     return "User object: \n{}\n{}\n{}\n{}\n{}\n{}\n".format(self.id, self.destination, self.description, self.travel_start_date, self.travel_end_date, self.creator)
