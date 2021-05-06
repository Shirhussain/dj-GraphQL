from django.contrib import admin
from .models import Question, Answer, Category, Quiz
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Category, CategoryAdmin)

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
    ]

class AnswerInline(admin.TabularInline):
    '''Tabular Inline View for Answer'''

    model = Answer
    fields = [
        'answer_text', 
        'is_right'
    ]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'quiz',)
    fields = ['title', 'quiz']
    inlines = [
        AnswerInline,
    ]

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'answer_text',
        'is_right',
        'question',
    ]

