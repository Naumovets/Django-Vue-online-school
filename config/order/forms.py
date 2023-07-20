from django import forms

from order.models import OrderItem
from user.models import CustomUser


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['curator'].queryset = CustomUser.objects.filter(groups__name='Куратор')