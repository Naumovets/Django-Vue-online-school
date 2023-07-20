from django.contrib import admin

from course.forms import CourseForm, CuratorForm
from course.models import Exam, Course, Webinar, Task, FileOfWebinar, Curator, Subject


class TaskInline(admin.StackedInline):
    model = Task
    extra = 1


class FileOfWebinarInline(admin.StackedInline):
    model = FileOfWebinar
    extra = 1


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title', )}


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('exam', 'title')
    prepopulated_fields = {'slug': ('title', 'exam')}
    search_fields = ('title', 'exam')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    form = CourseForm
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('subject', 'title', 'status', 'teacher', 'price', 'full_price')
    list_editable = ('price', 'full_price')
    search_fields = ('subject', 'title', 'status', 'teacher', 'description', 'price', 'full_price')
    ordering = ('title', 'subject', 'title', 'price', 'full_price')


@admin.register(Webinar)
class WebinarAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'title', 'date_start', 'code_of_translation')
    list_editable = ('title', 'date_start', 'code_of_translation')
    ordering = ('id', 'title', 'course', 'date_start')
    search_fields = ('title', 'course', 'date_start', 'code_of_translation')
    inlines = [FileOfWebinarInline, TaskInline]


@admin.register(Curator)
class CuratorAdmin(admin.ModelAdmin):
    form = CuratorForm
    list_display = ('curator', 'course')
    search_fields = ('curator', 'course')
