from django.contrib import admin
from .models import Hadith, ScholarLecture, Question


@admin.register(Hadith)
class HadithAdmin(admin.ModelAdmin):
    list_display = ('date', 'reference')
    search_fields = ('text', 'reference')


@admin.register(ScholarLecture)
class ScholarLectureAdmin(admin.ModelAdmin):
    list_display = ('title', 'scholar', 'date')
    list_filter = ('scholar', 'date')
    search_fields = ('title', 'description')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('user', 'asked_on', 'is_public', 'is_answered')
    list_filter = ('is_public', 'answered_on')
    search_fields = ('question', 'answer')

    def is_answered(self, obj):
        return bool(obj.answer)
    is_answered.boolean = True
