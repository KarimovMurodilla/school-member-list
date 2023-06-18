from django.contrib import admin

from .models import Pupil, Teacher, ClassNumber, Subject, Lesson, Feedback, Post


class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1


@admin.register(ClassNumber)
class ClassNumberAdmin(admin.ModelAdmin):
    list_display = ['class_number',]
    # inlines = [SubjectInline]


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    inlines = [LessonInline]


admin.site.register(Pupil)
admin.site.register(Teacher)
admin.site.register(Lesson)
admin.site.register(Feedback)
admin.site.register(Post)