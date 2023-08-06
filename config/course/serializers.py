from datetime import date

from rest_framework import serializers

from cart.models import CartItem
from course.models import Exam, Course, Webinar, Subject
from order.models import OrderItem, Order, ConfirmedCourse


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):

    def __init__(self, user=None, *args, **kwargs):
        self.user = user
        super(CourseSerializer, self).__init__(*args, **kwargs)

    status = serializers.SerializerMethodField()
    subject = serializers.SerializerMethodField()
    teacher = serializers.SerializerMethodField()
    isAddedToCart = serializers.SerializerMethodField()
    isAddedToOrder = serializers.SerializerMethodField()

    def get_isAddedToCart(self, obj):
        if self.user.cart.all().exists():
            cart = self.user.cart.get()
            if CartItem.objects.filter(cart=cart, course=obj).exists():
                return True
        return False

    def get_isAddedToOrder(self, obj):
        if self.user.order_courses.filter(course=obj).exists():
            return True
        return False

    def get_status(self, obj):
        return obj.get_status_display()

    def get_subject(self, obj):
        subject = obj.subject
        if subject:
            return {
                'slug': subject.slug,
                'title': subject.title,
                'exam': str(subject.exam)
            }
        return None

    def get_teacher(self, obj):
        teacher = obj.teacher
        if teacher:
            return {
                'first_name': teacher.first_name,
                'last_name': teacher.last_name,
                'image': teacher.image.url if teacher.image else None,
                'vk_link': teacher.vk_link
            }
        return None

    def get_fields(self):
        fields = super().get_fields()
        del fields['chat']
        return fields

    class Meta:
        model = Course
        fields = '__all__'


class WebinarSerializer(serializers.ModelSerializer):
    course = serializers.SerializerMethodField()
    files = serializers.SerializerMethodField()
    tasks = serializers.SerializerMethodField()

    def get_tasks(self, obj):
        tasks = obj.tasks.all()
        if tasks:
            return [
                {
                    'question': task.question,
                    'question_image': task.question_image.url if task.question_image else None,
                    'answer': task.answer,
                    'user_answer': None,
                    'solution': task.solution,
                    'solution_image': task.question_image.url if task.solution_image else None,
                    'id': task.id,
                    'is_multi_answer': False if task.answer else True,
                    'checkbox_answer_1': {'answer': task.checkbox_answer_1,
                                          'right': task.checkbox_right_answer_1,
                                          'user_answer': False
                                          },
                    'checkbox_answer_2': {'answer': task.checkbox_answer_2,
                                          'right': task.checkbox_right_answer_2,
                                          'user_answer': False
                                          },
                    'checkbox_answer_3': {'answer': task.checkbox_answer_3,
                                          'right': task.checkbox_right_answer_3,
                                          'user_answer': False
                                          },
                    'checkbox_answer_4': {'answer': task.checkbox_answer_4,
                                          'right': task.checkbox_right_answer_4,
                                          'user_answer': False
                                          },
                    'checkbox_answer_5': {'answer': task.checkbox_answer_5,
                                          'right': task.checkbox_right_answer_5,
                                          'user_answer': False
                                          },
                }
                for task in tasks
            ]
        else:
            return None

    def get_files(self, obj):
        files = obj.files.all()
        if files:
            return [
                {
                    'file_of_webinar': file.file_of_webinar.url,
                    'title': file.title
                }
                for file in files
            ]
        else:
            return None

    def get_course(self, obj):
        course = obj.course
        if course:
            return {'id': course.id,
                    'title': course.title,
                    'slug': course.slug,
                    'subject': course.subject.title,
                    'exam': str(course.subject.exam),
                    'status': course.get_status_display(),
                    'chat': course.chat,
                    'image': course.image.url,
                    'description': course.description,
                    'teacher': {'first_name': course.teacher.first_name,
                                'last_name': course.teacher.last_name,
                                'image': course.teacher.image.url if course.teacher.image else None,
                                'vk_link': course.teacher.vk_link},
                    'price': course.price
                    }
        return None

    class Meta:
        model = Webinar
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):
    exam = serializers.SerializerMethodField()

    def get_exam(self, obj):
        exam = str(obj.exam)
        return exam

    class Meta:
        model = Subject
        fields = '__all__'


class ConfirmedCourseSerializer(serializers.ModelSerializer):
    course = serializers.SerializerMethodField()
    curator = serializers.SerializerMethodField()
    webinars = serializers.SerializerMethodField()
    active = serializers.SerializerMethodField()

    def get_active(self, obj):
        end_date = obj.end_date
        if end_date:
            return end_date >= date.today()
        return False

    def get_curator(self, obj):
        curator = obj.curator
        if curator:
            return {
                'first_name': curator.user.first_name,
                'last_name': curator.user.last_name,
                'image': curator.user.image.url if curator.user.image else None,
                'vk_link': curator.user.vk_link
            }
        return None

    def get_course(self, obj):
        course = obj.course
        if course:
            return {'id': course.id,
                    'title': course.title,
                    'slug': course.slug,
                    'subject': course.subject.title,
                    'exam': str(course.subject.exam),
                    'status': course.get_status_display(),
                    'chat': course.chat,
                    'image': course.image.url,
                    'description': course.description,
                    'teacher': {'first_name': course.teacher.first_name,
                                'last_name': course.teacher.last_name,
                                'image': course.teacher.image.url if course.teacher.image else None,
                                'vk_link': course.teacher.vk_link},
                    'price': course.price
                    }
        return None

    def get_webinars(self, obj):
        webinars = obj.course.webinars.all()
        if webinars:
            return [
                {
                    'id': webinar.id,
                    'title': webinar.title,
                    'date_start': webinar.date_start
                }
                for webinar in webinars
            ]
        else:
            return None

    class Meta:
        exclude = 'user',
        model = ConfirmedCourse
