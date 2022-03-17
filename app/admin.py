from django.contrib import admin
from .models import *

# Register your models here.


class CompetitionAdmin(admin.ModelAdmin):
    list_display = ['date']


class ResultAdmin(admin.ModelAdmin):
    list_display = ['user', 'competition']


class ScrambleAdmin(admin.ModelAdmin):
    list_display = ['item_333']


admin.site.register(Competition, CompetitionAdmin)
admin.site.register(Result, ResultAdmin)
admin.site.register(Scramble, ScrambleAdmin)