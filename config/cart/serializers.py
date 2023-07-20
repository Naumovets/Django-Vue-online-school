from rest_framework import serializers


class CartItemSerializer(serializers.Serializer):
    course = serializers.SerializerMethodField()

    def get_course(self, obj):
        course = obj.course
        if course:
            return {
                'id': course.id,
                'title': course.title,
                'subject': str(course.subject),
                'status': str(course.get_status_display()),
                'price': course.price,
                'full_price': course.full_price,
                'teacher': {
                    'first_name': course.teacher.first_name,
                    'last_name': course.teacher.last_name,
                    'image': course.teacher.image.url if course.teacher.image else None,
                }
            }
        return None


class CartItemForPriceSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    period = serializers.CharField(max_length=10)
