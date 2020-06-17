from django.contrib import admin

# Register your models here.
from .models import SportsSession, Section

admin.site.register(SportsSession)
admin.site.register(Section)

