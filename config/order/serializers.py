from rest_framework import serializers

from course.serializers import CourseSerializer
from order.models import OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    course = serializers.SerializerMethodField()
    coupon = serializers.SerializerMethodField()
    curator = serializers.SerializerMethodField()
    webinars = serializers.SerializerMethodField()

    def get_curator(self, obj):
        curator = obj.curator
        if curator:
            return {
                'first_name': curator.first_name,
                'last_name': curator.last_name,
                'image': curator.image.url if curator.image else None,
                'vk_link': curator.vk_link
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
                                'image': course.teacher.image.url,
                                'vk_link': course.teacher.vk_link},
                    'price': course.price
                    }
        return None

    def get_coupon(self, obj):
        coupon = obj.coupon
        if coupon:
            return {'code': coupon.code,
                    'discount': coupon.discount}
        return None

    def get_webinars(self, obj):
        webinars = obj.course.webinars.all()
        return [
            {
                'id': webinar.id,
                'title': webinar.title,
                'code': webinar.code_of_translation
            }
            for webinar in webinars
        ]

    class Meta:
        exclude = 'order',
        model = OrderItem
