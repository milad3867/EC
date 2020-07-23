from django.contrib import admin
from project.apps.userManager.models import Profile, Course, Assignment, Ticket
# Register your models here.
admin.site.register(Profile)
admin.site.register(Course)
admin.site.register(Assignment)
admin.site.register(Ticket)
