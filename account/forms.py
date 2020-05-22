from django.contrib.auth.models import User
from django import forms
from .models import UserReg
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                                widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')

    def clean_confirm_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['confirm_password']:
            raise forms.ValidationError('Oops! your passwords do not match.')
        return cd['confirm_password']

class UserAddtnlForm(forms.ModelForm):
    class Meta:
        model=UserReg
        fields=['mobile_num',]

class UpdateEmailForm(forms.Form):
    email=forms.EmailField(max_length=150)
    confirm_email=forms.EmailField(max_length=150)
    # 
    # def clean_confirm_email(self):
    #     cd = self.cleaned_data
    #     if cd['email'] != cd['confirm_email']:
    #         raise forms.ValidationError('Oops! your email do not match.')
    #     return cd['confirm_email']
