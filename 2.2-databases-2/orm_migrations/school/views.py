from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    students = Student.objects.prefetch_related('teacher').all()
    object_list = [{'student': student, 'teachers': student.teacher.all()} for student in students]
    context = {
        'object_list': object_list
    }
    return render(request, template, context)
