from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(HomePage)


# An admin interface for the Demand model
class DemandAdmin(admin.ModelAdmin):
    list_display = ('profession','year','salary','vacancies')

admin.site.register(Demand, DemandAdmin)


# An admin interface for the Geography model
class GeographyAdmin(admin.ModelAdmin):
    list_display = ('city','salary','vacancies_percentage')

admin.site.register(Geography, GeographyAdmin)


# An admin interface for the Skills model
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('profession','year','key_skills')

admin.site.register(Skills, SkillsAdmin)


# An admin interface for the latest jobs model
@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'salary', 'region', 'date')
    ordering = ('-date',)
    search_fields = ('name', 'company', 'region')
    

