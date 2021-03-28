from django.contrib import admin

# Register your models here.
from .models import ExtendedUser, Enrolment

admin.site.register(ExtendedUser)
admin.site.register(Enrolment)
