"""MCQ_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mcq_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name = 'home'),
    path('logout/', logoutUser, name = 'logout'),
    path('StudentPage/', StudentPage, name = 'student'),
    path('TeacherPage/', TeacherPage, name = 'teacher'),
    path('register/', registerPage),
    path('TeacherPage/add_category/', add_category, name = 'add_category'),
    path('TeacherPage/add_question/', add_question, name = 'add_question'),
    path('TeacherPage/everything/', everything, name = 'everything'),
    path('TeacherPage/generate/', cat_amount, name = 'generate'),
    path('TeacherPage/randomise/', get_random, name = 'randomise'),
    path('TeacherPage/add_answer/', add_answer, name = 'add_answer'),
    path('TeacherPage/test/', test, name = 'test'),
    
    
]
