from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']

class Add_Question_Form(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'category',
            'text'
        ]


class Add_Answer_Form(forms.ModelForm):
    class Meta:
        model = Answer
        fields = [
            'question',
            'a',
            'b',
            'c',
            'correct'
        ]

class Add_Category_Form(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'title',
            'topic'
        ]
        
class Cat_Amount_Form(forms.ModelForm):
    class Meta:
        model = Cat_Amount 
        fields = ['template', 'category', 'quantity']

class Template(forms.ModelForm):
    class Meta:
        model = Template
        fields = ['name']