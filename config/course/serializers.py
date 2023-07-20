from rest_framework import serializers

from cart.models import CartItem
from course.models import Exam, Course, Webinar, Subject


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
    isAdded = serializers.SerializerMethodField()

    def get_isAdded(self, obj):
        if self.user.cart.all().exists():
            cart = self.user.cart.get()
            if CartItem.objects.filter(cart=cart, course=obj).exists():
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
