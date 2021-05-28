from django import forms
import datetime
from django.core.exceptions import ValidationError

from app_profiles.models import User


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields =  '__all__'







    # username = forms.CharField(min_length=3)
    # password = forms.CharField()
    # first_name = forms.CharField()
    # second_name = forms.CharField()
    # last_name = forms.CharField()
    # email = forms.EmailField()
    # birthday = forms.DateField()

    # def clean_birthday(self):
    #     data = self.cleaned_data['birthday']
    #     today = datetime.date.today()
    #     year_delta = (today - data).days /365
    #     if year_delta < 18:
    #         raise ValidationError('Нет 18 лет')
    #     return data
    #
    # def clean(self):
    #     cleaned_data = super(UserForm, self).clean()
    #     first_name = cleaned_data.get('first_name')
    #     last_name = cleaned_data.get('last_name')
    #     if first_name =='Иван' and last_name == 'Иванов':
    #         msg = 'Нельзя регистрироваться Ивану Иванову'
    #         self.add_error('first_name', msg)
    #         self.add_error('last_name', msg)
