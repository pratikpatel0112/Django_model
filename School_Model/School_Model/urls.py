"""School_Model URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from student import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('index',views.index),
    path('studlist',views.studentlist),
    path('add',views.add.as_view()),
    path('update/<int:id>',views.update.as_view()),
    path('delete/<int:id>',views.delete),
    path('nameaes',views.nameaes),
    path('namedesc',views.namedesc),
    path('emailaes',views.emailaes),
    path('emaildesc',views.emaildesc),
    path('feesaes',views.feesaes),
    path('feesdesc',views.feesdesc),
    path('student/searchbyname',views.searchbyname),
]
