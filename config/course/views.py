from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
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


# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
# class WebinarView(APIView):
#     """ Просмотр вебинара """
#     def get(self, request, code):
#         user = request.user
#         order = get_object_or_404(Order,
#                                   user=user)
#         webinar = get_object_or_404(Webinar,
#                                     code_of_translation=code)
#         course_slug = webinar.course.slug
#
#         curator = get_object_or_404(OrderItem,
#                                        order=order,
#                                        course__slug=course_slug).curator
#
#         webinar_serialized = WebinarSerializer(webinar)
#         return Response({'webinar': webinar_serialized.data,
#                          'curator': {'first_name': curator.first_name,
#                                      'last_name': curator.last_name,
#                                      'image': curator.image.url,
#                                      'vk_link': curator.vk_link}})

# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
# class OrderItemsView(APIView):
#     """ Просмотр всех купленных курсов """
#     def get(self, request):
#         user = request.user
#         if Order.objects.filter(user=user).exists():
#             order = Order.objects.get(user=user)
#             order_items = order.items.all()
#             order_items_serialized = OrderItemSerializer(order_items, many=True)
#             return Response(order_items_serialized.data)
#         else:
#             return Response({'response': 'Курсов нет'})

# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
# class OrderItemView(APIView):
#     """ Просмотр оплаченного курса """
#     def get(self, request, slug):
#         user = request.user
#         order = get_object_or_404(Order,
#                                   user=user)
#         order_item = get_object_or_404(OrderItem,
#                                        order=order,
#                                        course__slug=slug)
#         order_items_serialized = OrderItemSerializer(order_item)
#         return Response(order_items_serialized.data)
#