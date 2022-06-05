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
from app.views import home, form, form1, cad, create, create1, view, edit, edit1, update, update1, delete, delete1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('form/', form, name='form'),
    path('form1/', form1, name='form1'),
    path('cad/', cad, name='cad'),
    path('create/', create, name='create'),
    path('create1/', create1, name='create1'),
    path('view/<int:pk>/', view, name='view'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('edit1/<int:pk>/', edit1, name='edit1'),
    path('update/<int:pk>/', update, name='update'),
    path('update1/<int:pk>/', update1, name='update1'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('delete1/<int:pk>/', delete1, name='delete1'),
]
