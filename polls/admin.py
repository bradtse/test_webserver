from django.contrib import admin
from polls.models import Poll
from polls.models import Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class PollAdmin(admin.ModelAdmin):
    list_display = ('question', 'pub_date', 'was_published_recently')
    fieldsets = [
        (None, {'fields': ['question']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date', 'question']
    search_fields = ['question']

admin.site.register(Poll, PollAdmin)
