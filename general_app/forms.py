from django import forms
from general_app.models import Contact, User


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ['timestamp', 'user_ip']

        labels = {
            'user_name' : 'نام و نام خانوادگی',
            'user_email' : 'آدرس ایمیل',
            'message_subject' : 'موضوع پیام',
            'message_content' : 'متن پیام',
        }

        widgets = {
            'user_name': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-rose-500 focus:border-rose-500',
                'placeholder': 'مثال: علی احمدی'
            }),
            'user_email': forms.EmailInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-rose-500 focus:border-rose-500',
                'placeholder': 'example@email.com'
            }),
            'message_subject': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-rose-500 focus:border-rose-500',
                'placeholder': 'مثال: گزارش خطا'
            }),
            'message_content': forms.Textarea(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-rose-500 focus:border-rose-500',
                'placeholder': 'پیام خود را اینجا بنویسید...',
                'rows': '5'
            }),
        }



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"

        labels ={
            'user_name': 'نام و نام خانوادگی',
            'user_email': 'آدرس ایمیل',
            'user_password': 'رمز عبور',
            'password_repetition': 'تکرار رمز عبور',
        }

        widgets = {
            'user_name': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-rose-500 focus:border-rose-500',
                'placeholder': 'نام کامل شما'
            }),
            'user_email': forms.EmailInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-rose-500 focus:border-rose-500',
                'placeholder': 'example@email.com'
            }),
            'user_password': forms.PasswordInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-rose-500 focus:border-rose-500',
                'placeholder': 'حداقل ۸ کاراکتر'
            }),
            'password_repetition' : forms.PasswordInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-rose-500 focus:border-rose-500',
                'placeholder': 'تکرار رمز عبور'
            })
        }
