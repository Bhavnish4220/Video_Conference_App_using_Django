from django.contrib import admin
from .models import MyFile
# Register your models here.
@admin.register(MyFile)
class MyFileAdmin(admin.ModelAdmin):
    list_display = ['id', 'file', 'date']