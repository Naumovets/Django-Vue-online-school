from django.http import Http404
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from course.models import Exam, Course, Subject, Webinar
from course.serializers import ExamSerializer, CourseSerializer, SubjectSerializer, WebinarSerializer, \
    ConfirmedCourseSerializer
from order.models import ConfirmedCourse


class ExamsView(APIView):

    def get(self, request):
        exam = Exam.objects.all()
        serialized_exams = ExamSerializer(exam, many=True)

        return Response(serialized_exams.data)


class CoursesView(APIView):

    def get(self, request):
        courses = Course.objects.all()
        serialized_courses = CourseSerializer(user=request.user, instance=courses, many=True)
        return Response(serialized_courses.data)


class FreeCoursesView(APIView):

    def get(self, request):
        courses = Course.objects.filter(status=Course.Status.FREE)
        serialized_courses = CourseSerializer(user=request.user, instance=courses, many=True)
        return Response(serialized_courses.data)


class SubjectsView(APIView):

    def get(self, request):
        subjects = Subject.objects.all()
        serialized_subjects = SubjectSerializer(subjects, many=True)
        return Response(serialized_subjects.data)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class WebinarView(APIView):
    """ Просмотр вебинара """
    def get(self, request, code):
        user = request.user
        webinar = get_object_or_404(Webinar,
                                    code_of_translation=code)
        course_slug = webinar.course.slug

        curator = get_object_or_404(ConfirmedCourse,
                                    user=user,
                                    course__slug=course_slug).curator

        webinar_serialized = WebinarSerializer(webinar)
        return Response({'webinar': webinar_serialized.data,
                         'curator': {'first_name': curator.user.first_name,
                                     'last_name': curator.user.last_name,
                                     'image': curator.user.image.url if curator.user.image else None,
                                     'vk_link': curator.user.vk_link} if curator else None})


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class ConfirmedCoursesView(APIView):
    """ Просмотр всех купленных курсов """
    def get(self, request):
        user = request.user
        if ConfirmedCourse.objects.filter(user=user).exists():
            courses = ConfirmedCourse.objects.filter(user=user)
            courses_serialized = ConfirmedCourseSerializer(courses, many=True)
            return Response(courses_serialized.data)
        else:
            return Http404()


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class ConfirmedCourseView(APIView):
    """ Просмотр оплаченного курса """
    def get(self, request, slug):
        user = request.user
        course = get_object_or_404(ConfirmedCourse, user=user, course__slug=slug)
        course_serialized = ConfirmedCourseSerializer(course)
        return Response(course_serialized.data)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class CalendarWebinar(APIView):
    def get(self, request):
        user = request.user
        confirmed_courses = ConfirmedCourse.objects.filter(user=user)
        result = []
        for confirmed_course in confirmed_courses:
            for webinar in confirmed_course.course.webinars.all():
                result.append({'title': webinar.title + ' ('+ str(webinar.course) + ')',
                'start': webinar.date_start, 
                'url': 'webinar/' + webinar.code_of_translation})

        return Response(result)
