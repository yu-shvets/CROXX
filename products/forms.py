from django import forms
from .models import CustomerEmail


class CustomerEmailForm(forms.ModelForm):

    class Meta:
        model = CustomerEmail
        fields = '__all__'


