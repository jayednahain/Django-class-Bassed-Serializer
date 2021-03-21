
from django.contrib import admin
from django.urls import path,include
from class_based_views import views


urlpatterns = [
   path('student/',views.StudentListView.as_view()),
   path('student/<int:pk>',views.StudentDetailView.as_view())
]

