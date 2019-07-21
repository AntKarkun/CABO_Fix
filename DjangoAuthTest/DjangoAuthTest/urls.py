"""DjangoAuthTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from myapp.views import index, login_page, register, logout_page, all_problem, my_problems, all_admin, admin_my_problems

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index.html', index),
    path('login', login_page),
    path('logout', logout_page),
    path('register', register),

    path('', all_problem),
    path('my_problems.html', my_problems),
    path('admin.html', all_admin),
    # path('all_admin.html', all_admin)
    path('admin_my_problems.html', admin_my_problems),
]
