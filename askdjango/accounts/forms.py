from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Profile

# 회원가입 UserCreationForm 커스텀

# case1. email 입력 받기
class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ('username', 'email')

# class SignupForm(UserCreationForm):
#     phone_number = forms.CharField()
#     address = forms.CharField()
#
#     class Meta(UserCreationForm.Meta):
#         fields = UserCreationForm.Meta.fields + ('email',)
#
#     def save(self):
#         user = super().save()
#         profile = Profile.objects.create(
#             user = user,
#             phone_number = self.cleaned_data['phone_number'],
#             address = self.cleaned_data['address'])
#         return user


class LoginForm(AuthenticationForm):
    answer = forms.IntegerField(label='3+3=?')

    def clean_answer(self):
        answer = self.cleaned_data.get('answer', None)
        if answer != 6:
            raise forms.ValidationError('mismatched!')
        return answer