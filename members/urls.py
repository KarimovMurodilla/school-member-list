"""
URL configuration for school project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from .views import (
        HomeListView, AboutListView,
        TeacherListView, PupilListView, 
        ContactListView, EtiquetteListView, 
        ClassNumberListView, SubjectDetailView,
        FeedbackCreateView
    )

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('about/', AboutListView.as_view(), name='about'),
    path('teachers/', TeacherListView.as_view(), name='teachers'),
    path('pupils/', PupilListView.as_view(), name='pupils'),
    path('contact/', ContactListView.as_view(), name='contact'),
    path('etiquette/', EtiquetteListView.as_view(), name='etiquette'),
    path('subject/', ClassNumberListView.as_view(), name='subject'),
    path('lesson/<int:pk>/<str:slug>/', SubjectDetailView.as_view(), name='lesson'),
    path('feedback/', FeedbackCreateView.as_view(), name='feedback'),
]