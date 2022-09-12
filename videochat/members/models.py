from django.db import models

# Create your models here.
class Members(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, default=None)
    isadmin = models.BooleanField(default=False)
    isvisible = models.BooleanField(default=False)
    issignedin = models.BooleanField(default=False)
    showemail = models.BooleanField(default=False)
    showfullname = models.BooleanField(default=False)
    passwordsaved = models.BooleanField(default=False)
    creationdate = models.DateTimeField(auto_now=True)
    resetToken = models.CharField(max_length=255)
    expireToken = models.CharField(max_length=255)
