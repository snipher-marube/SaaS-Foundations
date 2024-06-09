from django.contrib import admin

from .models import PageVisits

@admin.register(PageVisits)
class PageVisitsAdmin(admin.ModelAdmin):
    list_display = ['path', 'timestamp']
    search_fields = ['path']
    list_filter = ['timestamp']