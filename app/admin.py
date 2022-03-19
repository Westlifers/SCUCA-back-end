from django.contrib import admin
from .models import *

# Register your models here.


class CompetitionAdmin(admin.ModelAdmin):
    list_display = ['date', 'item_222', 'item_333', 'item_444', 'item_555', 'item_666', 'item_777']


class ResultAdmin(admin.ModelAdmin):
    list_display = ['user', 'competition', 'item', 'time1', 'time2', 'time3', 'time4', 'time5']


admin.site.register(Competition, CompetitionAdmin)
admin.site.register(Result, ResultAdmin)