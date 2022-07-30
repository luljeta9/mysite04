# Register your models here.
# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']
# admin.site.register(Question, QuestionAdmin)

from django.contrib import admin
from .models import Choice, Question


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]


class ChoiceInline(admin.TabularInline):  # StackedInline
    model = Choice
    extra = 3


inlines = [ChoiceInline]
admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
