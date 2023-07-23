from django import forms

from course.models import Curator, Course
from order.models import ConfirmedCourse
from user.models import CustomUser


class ConfirmedCourseForm(forms.ModelForm):
    class Meta:
        model = ConfirmedCourse
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            self.fields['curator'].queryset = Curator.objects.filter(course=self.instance.course)
        except ConfirmedCourse.course.RelatedObjectDoesNotExist:
            ...
