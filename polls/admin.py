from django.contrib import admin

from .models import Town
from .models import Choice

from django.contrib import admin

from .models import Town


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class TownAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_display = ('question_text','pub_date','was_published_recently')
    inlines = [ChoiceInline]
    list_filter = ['pub_date']

admin.site.register(Town, TownAdmin)




# Register your models here.
