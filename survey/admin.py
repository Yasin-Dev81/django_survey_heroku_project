from django.contrib import admin
from . import models


# TabularInlines
class SurveyTitleInline(admin.TabularInline):  # TabularInline
    model = models.SurveyTitle
    fields = [
        'title_text',
        'description',
        'author'
    ]


class SurveyQuestionInline(admin.TabularInline):  # TabularInline
    model = models.SurveyQuestion
    fields = [
        'question_text',
        'title',
    ]


class SurveyOptionInline(admin.TabularInline):  # TabularInline
    model = models.SurveyOption
    fields = [
        'option_text',
        'question',
    ]


class SurveyAnswerInline(admin.TabularInline):  # TabularInline
    model = models.SurveyAnswer
    fields = [
        'option',
        'author',
    ]


# admin panels
@admin.register(models.SurveyTitle)
class SurveyTitleAdmin(admin.ModelAdmin):
    list_display = [
        'title_text',
        'author',
        'datetime_created'
    ]
    list_filter = ['datetime_created']
    ordering = ['datetime_created']

    inlines = [
        SurveyQuestionInline
    ]


@admin.register(models.SurveyQuestion)
class SurveyQuestionAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'question_text',
        'datetime_created'
    ]
    list_filter = ['title']
    ordering = ['title']

    inlines = [
        SurveyOptionInline
    ]


@admin.register(models.SurveyOption)
class SurveyOptionAdmin(admin.ModelAdmin):
    list_display = [
        'question',
        'option_text',
        'datetime_created'
    ]
    list_filter = ['question']
    ordering = ['question']

    inlines = [
        SurveyAnswerInline
    ]


@admin.register(models.SurveyAnswer)
class SurveyAnswerAdmin(admin.ModelAdmin):
    list_display = [
        'option',
        'author',
        'datetime_created'
    ]
    list_filter = ['datetime_created']
    ordering = ['datetime_created']
