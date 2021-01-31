from django.contrib import admin

from .models import Question, Choice


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'pub_date']

# alternatywnie
# admin.site.register(Question)
# admin.site.register(Choice)

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):

    raw_id_fields = [
        'question',
    ]

    list_display = [
        'question',
        'choice_text',
        'votes',
    ]

    search_fields = [
        'question__question_text',
        'choice_text',
    ]
