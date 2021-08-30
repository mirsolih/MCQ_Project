from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.db.models import OuterRef,F
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from django .contrib.auth.models import Group
from .models import *

# Create your views here.
def add_category(request):
    form = Add_Category_Form(request.POST or None)
    if form.is_valid():
        form.save()
        form = Add_Category_Form()
        messages.success(request, 'The category is succesfully added into the database')
        return redirect('teacher')
    context = {
        'form': form
    }
    return render(request, 'mcq_app/add_category.html', context)

def add_question(request):
    form = Add_Question_Form(request.POST or None)
    if form.is_valid():
        form.save()
        form = Add_Question_Form()
        messages.success(request, 'The question is succesfully added into the database')
        return redirect('teacher')
    context = {
        'form': form
    }
    return render(request, 'mcq_app/add_question.html', context)


def add_answer(request):
    form = Add_Answer_Form(request.POST or None)
    if form.is_valid():
        form.save()
        form = Add_Answer_Form()
        messages.success(request, 'The answer is succesfully added into the database')
        return redirect('teacher')
    context = {
        'form': form
    }
    return render(request, 'mcq_app/add_answer.html', context)

def add_category(request):
    form = Add_Category_Form(request.POST or None)
    if form.is_valid():
        form.save()
        form = Add_Category_Form()
        messages.success(request, 'The category is succesfully added into the database')
        return redirect('teacher')
    context = {
        'form': form
    }
    return render(request, 'mcq_app/add_category.html', context)

def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('student')
        else:
            messages.info(request, 'Username or Password is incorrect!')
        
    context = {}
    return render(request, 'mcq_app/login.html')

def logoutUser(request):
    logout(request)
    return redirect('home')


@login_required(login_url = 'home')
@allowed_users(allowed_roles = ['student', 'admin'])
def StudentPage(request):
    return render(request, 'mcq_app/StudentPage.html')

@login_required(login_url = 'home')
@admin_only
def TeacherPage(request):
    category = Category.objects.all()
    return render(request, 'mcq_app/TeacherPage.html', {'category': category, 'cat_amount': cat_amount} )

#@unauthenticated_user
@admin_only
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name = 'student')
            user.groups.add(group)

            messages.success(request, 'Account has successfully created for ' + username)

            return redirect('teacher')

    context = {'form':form}
    return render(request, 'mcq_app/register.html', context)

def everything(request):
    question = Question.objects.all()
    answer = Answer.objects.all()

    context = {'question': question, 'answer': answer}

    return render(request, 'mcq_app/everything.html', context)

def cat_amount(request):
    cat_amount = Cat_Amount.objects.all()
    template = Template.objects.all()
    test = Test.objects.all()
    form = Cat_Amount_Form(request.POST or None)
    if form.is_valid():
        form.save()
        form = Cat_Amount_Form()
        messages.success(request, 'The data is succesfully added into the database')
        return redirect('generate')
    context = {
        'form': form,
        'cat_amount': cat_amount,
        'template': template,
        'test': test
    }
    return render(request, 'mcq_app/GenerateTest.html', context)

def get_random(request):
    cat_amount = Cat_Amount.objects.all()
    answer = Answer.objects.order_by('?')[:2]
  
    context = {'answer': answer, 'cat_amount': cat_amount}
    return render(request, 'mcq_app/randomise.html', context)

def test(request):
    test = Test.objects.filter(name__exact = 'Template 2 test')
    cat_amount = Cat_Amount.objects.filter(template__name__exact = 'Template 2')
    answer = Answer.objects.filter(question__category__topic__exact = 'Datatypes')
    
    
    context = {'test': test,'cat_amount': cat_amount, 'answer': answer}
    return render(request,'mcq_app/test.html', context)



