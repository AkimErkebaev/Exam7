from django.contrib import admin

# Register your models here.
from webapp.models import Poll, Choice, Answer


class PollAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']
    list_display_links = ['name']
    list_filter = ['created_at']
    search_fields = ['created_at']
    fields = ['name']
    readonly_fields = []
    filter_horizontal = []


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
admin.site.register(Answer)