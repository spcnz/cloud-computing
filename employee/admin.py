from django.contrib import admin

from . import models


@admin.register(models.Employee)
class EmployeeAdmin(admin.ModelAdmin):
    date_hierarchy = 'birth_date'
    list_display = [
        'name',
        'surname',
        'salary',
        'birth_date'
    ]
    search_fields = ['name']

@admin.register(models.Counter)
class CounterAdmin(admin.ModelAdmin):
    list_display = [
        'value'
    ]