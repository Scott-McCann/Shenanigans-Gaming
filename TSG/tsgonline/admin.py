from django.contrib import admin
from .models import TeamMember, StaffMember, Article

# Register your models here.
admin.site.register(TeamMember)
admin.site.register(StaffMember)
admin.site.register(Article)
