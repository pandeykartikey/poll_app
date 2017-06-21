# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Question, Choice


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_display = ('question_text', 'pub_date')

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)