from django import forms

from course.models import Course, Curator
from user.models import CustomUser


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['teacher'].queryset = CustomUser.objects.filter(groups__name='Преподаватель')


class CuratorForm(forms.ModelForm):
    class Meta:
        model = Curator
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = CustomUser.objects.filter(groups__name='Куратор')
        