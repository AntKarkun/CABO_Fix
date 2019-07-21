from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from myapp.models import Сomplaint


def index(request):
    # если мы залогинены
    if request.user.is_authenticated:
        if request.method == 'GET':
            problems_nr = Сomplaint.objects.filter(resheno=False, reshaetsa=False)
            problems_r = Сomplaint.objects.filter(resheno=False, reshaetsa=True)

            return render(request, 'index.html', {'problems_nr': problems_nr, 'problems_r': problems_r})
        elif request.method == 'POST':
            if request.POST['submit'] == 'Отправить':
                compl = Сomplaint()
                compl.namee = request.POST['probl_name']
                user = User.objects.get(id=request.user.id)
                compl.author = user
                compl.room = request.POST['room']
                compl.problema = request.POST['Obr']
                compl.save()
                return redirect('/')

    else:
        return redirect('/login')


def login_page(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST.get('login', '')
        password = request.POST.get('password', '')

        if username == '' or password == '':
            return HttpResponse("Заполните все поля")

        # проверяем правильность логина и пароля
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse("Логин неверен")


def register(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'register.html')
    if request.method == 'POST':
        username = request.POST.get('login', '')
        password = request.POST.get('password', '')
        email = request.POST.get('email', '')
        # name = request.POST.get('name', '')

        if username == '' or password == '' or email == '':
            return HttpResponse("Заполните все поля")

        if User.objects.filter(username=username).exists():
            return HttpResponse("Логин занят")

        # создаем пользователя
        user = User.objects.create_user(username, email, password)
        user.save()

        # "входим" пользователя
        login(request, user)

        return redirect('/')


def logout_page(request):
    if request.method == 'POST':
        logout(request)
    return redirect('/')


def all_problem(request):
    if request.method == 'GET':
        if request.user.groups.filter(name="Moders"):
            return redirect('admin.html')

        problems_nr = Сomplaint.objects.filter(resheno=False, reshaetsa=False)
        problems_r = Сomplaint.objects.filter(resheno=False, reshaetsa=True)

        return render(request, 'all_problem.html', {'problems_nr': problems_nr, 'problems_r': problems_r})


def my_problems(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            problems = Сomplaint.objects.filter(resheno=False, author=request.user)

            return render(request, 'my_problems.html', {'problems': problems})
        else:
            return redirect('/login')


def all_admin(request):
    if request.user.groups.filter(name="Moders"):
        problems_nr = Сomplaint.objects.filter(resheno=False, reshaetsa=False)

        if request.method == 'GET':

            a = 'all_admin.html'
            return render(request, a, {'problems_nr': problems_nr, 'user': request.user})

        if request.method == 'POST':
            if request.POST['submit'] == 'Взять проблему':
                problem_nr = Сomplaint.objects.get(pk=request.POST['hidden'])
                problem_nr.reshaetsa = True
                problem_nr.fixer = request.user.username
                problem_nr.save()
                return redirect('admin_my_problems.html')
    else:
        return redirect('/')


def admin_my_problems(request):
    if request.user.groups.filter(name="Moders"):
        problems_r = Сomplaint.objects.filter(resheno=False, reshaetsa=True, fixer=request.user.username)

        if request.method == 'GET':
            return render(request, 'admin_my_problems.html', {'problems_r': problems_r})
        if request.method == 'POST':
            if request.POST['submit'] == 'Закончить выполнение':
                problem_r = Сomplaint.objects.get(pk=request.POST['hidden'])
                problem_r.delete()
                return redirect('/admin.html')

    else:
        return redirect('/')
