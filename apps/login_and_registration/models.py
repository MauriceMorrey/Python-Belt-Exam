# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# import bcrypt
import re
NAME_REGEX = re.compile(r"^[-a-zA-Z']+$")
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")


class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData["first_name"]) < 1:
			errors["first_name"] = "First name field cannot be left blank"
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name should contain at least 2 characters"
        if not NAME_REGEX.match(postData["first_name"]):
			errors["first_name"] = "First name contains invalid characters."
        if len(postData["last_name"]) < 1:
			errors["last_name"] = "Last name field cannot be left blank"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name should contain at least 2 characters"
        if not NAME_REGEX.match(postData["last_name"]):
			errors["last_name"] = "Last name contains invalid characters."
        if len(postData["email"]) < 1:
			errors["email"] = "Email address field cannot be left blank."
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address. Please enter a valid email address."
        if self.filter(email=postData["email"]):
			errors["email"] = "Email address exists. Please use a different email address."
        if len(postData["password"]) < 8:
			errors["password"] = "Password should contain at least eight characters."
        if not postData["password"] == postData["password_confirmation"]:
			errors["password"] = "Password and password confirmation do not match."
        if len(postData["date_hired"])==0:
            errors["date_hired"] = "Date cannot be empty!"
        print postData["date_hired"]
        now = datetime.now().strftime("%Y-%m-%d")
        if now > postData['date_hired']:
            errors['date_hired'] = "Must select a future date"
        return errors

    def login_validator(self, postData):
        errors = {}
        if len(postData["email"]) < 1:
            errors['email'] = "Invalid information. Please enter valid information"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid information. Please enter valid information"
        if not self.filter(email=postData["email"]):
            errors['email'] = "Invalid information. Please enter valid information"
        if len(postData["password"]) < 8:
            errors['email'] = "Invalid information. Please enter valid information"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    date_hired = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()


    def __str__(self):
        return self.first_name  +  self.last_name

    def __repr__(self):
        return "User object: \n{}\n{}\n{}\n{}\n".format(self.id, self.first_name, self.last_name, self.email)