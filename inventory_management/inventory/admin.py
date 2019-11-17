from django.contrib import admin
#from import_export.admin import ImportExportModelAdmin
from .models import *

@admin.register(Resturant)
class ViewAdmin(admin.ModelAdmin):
    pass
    #exclude = ('id', )

# Register your models here.
