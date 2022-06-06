"""MR66 URL Configuration

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
from app.views import home, form, form1, form2, cad, hist, create, create1, create2, view, edit, edit1, edit2, update, update1, update2, delete, delete1, delete2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('form/', form, name='form'),
    path('form1/', form1, name='form1'),
    path('form2/', form2, name='form2'),
    path('cad/', cad, name='cad'),
    path('hist/', hist, name='hist'),
    path('create/', create, name='create'),
    path('create1/', create1, name='create1'),
    path('create2/', create2, name='create2'),
    path('view/<int:pk>/', view, name='view'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('edit1/<int:pk>/', edit1, name='edit1'),
    path('edit2/<int:pk>/', edit2, name='edit2'),
    path('update/<int:pk>/', update, name='update'),
    path('update1/<int:pk>/', update1, name='update1'),
    path('update2/<int:pk>/', update2, name='update2'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('delete1/<int:pk>/', delete1, name='delete1'),
    path('delete2/<int:pk>/', delete2, name='delete2'),
]
