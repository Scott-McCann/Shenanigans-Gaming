from django.db import models

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
