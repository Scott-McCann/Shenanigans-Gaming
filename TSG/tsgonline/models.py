from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class TeamMember(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    biography = models.TextField(default="biography")

    def __str__(self):
        return self.first_name

class StaffMember(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    title = models.CharField(max_length=256, default="?")
    biography = models.TextField(default="staff")

    def __str__(self):
        return self.first_name

class Article(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField(default="content")
    date_added = models.DateTimeField(auto_now_add=True, db_index=True)
    is_shown =  models.BooleanField(null=False, default=False, db_index=True)

    def __str__(self):
        return self.title
