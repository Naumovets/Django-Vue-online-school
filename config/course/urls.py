from django.urls import path

from course.views import ExamsView, CoursesView, SubjectsView, FreeCoursesView, ConfirmedCoursesView, \
    ConfirmedCourseView, WebinarView, CalendarWebinar

app_name = 'course'

urlpatterns = [
    path('exams', ExamsView.as_view(), name='exams'),
    path('courses', CoursesView.as_view(), name='courses'),
    path('free-courses', FreeCoursesView.as_view(), name='free_courses'),
    path('subjects', SubjectsView.as_view(), name='subjects'),\
    path('get-courses', ConfirmedCoursesView.as_view(), name='get-courses'),
    path('webinar/<int:id>', WebinarView.as_view(), name='webinar'),
    path('calendar_webinar', CalendarWebinar.as_view(), name='calendar_webinar'),
    path('<int:id>', ConfirmedCourseView.as_view(), name='course'),
]
