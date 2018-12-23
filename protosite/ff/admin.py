from django.contrib import admin
from .models import FSentence

# Register your models here.
# adds data IOing to the admin interface
admin.site.register(FSentence)
