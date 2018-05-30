from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
from bcrypt import checkpw
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class userManager(models.Manager):
    def validator(self, postData):
        # match_email is grabbing the email that is within the db , that the user posted
        match_email = User.objects.filter(email = postData['email'])
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = 'First name must be longer than 2 characters'
        if len(postData['last_name']) < 2:
            errors['last_name'] = 'Last name must be longer than 2 characters'
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'email is invalid'
        #  if the email is greater than 0, it means that it is within the DB, which means email is already in use.
        if len(match_email) > 0:
            errors['email'] = 'Email is already in use, please use another email'
        if len(postData['email']) < 1:
            errors['email'] = 'Email cannot be empty'
        if postData['password'] != postData['confirm_password']:
            errors['confirm_password'] = 'Passwords do not match'
        if len(postData['password']) < 6:
            errors['password'] = 'Passwords must be longer than 6 characters'
        return errors
    def login_validation(self, postData):
        errors = {}
        if len(postData['password']) < 1:
            errors['password'] = "password cannot be empty"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Email is not in correct format"
        else:
            # this matches the login email with the email that is posted within the database
            match_email = User.objects.filter(email = postData['email'])
            #  if the match email is greater than 0, meaning it's within the database, the email is a match and you may now login
            if len(match_email) > 0:
                print('matched email')
    #  if the posted password matches the password within the DB, password is valid 
                if checkpw(postData['password'].encode(), match_email[0].password.encode()):
                    print('matched password')
                else:
                    errors['email'] ='Email is invalid'                        
                    errors['password'] ='Password is invalid'
            else: 
                errors['email'] = 'Please register first'
        return errors

class User(models.Model):
    first_name = models.CharField(max_length= 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    objects = userManager()