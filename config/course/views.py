from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from course.models import Exam, Course, Subject
from course.serializers import ExamSerializer, CourseSerializer, SubjectSerializer


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


