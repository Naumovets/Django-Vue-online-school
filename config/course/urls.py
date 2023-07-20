from django.urls import path

from course.views import ExamsView, CoursesView, SubjectsView, FreeCoursesView

app_name = 'course'

urlpatterns = [
    path('exams', ExamsView.as_view(), name='exams'),
    path('courses', CoursesView.as_view(), name='courses'),
    path('free-courses', FreeCoursesView.as_view(), name='free_courses'),
    path('subjects', SubjectsView.as_view(), name='subjects'),
]