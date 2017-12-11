from django.contrib import admin
from .models import TeamMember, StaffMember

# Register your models here.
admin.site.register(TeamMember)
admin.site.register(StaffMember)
