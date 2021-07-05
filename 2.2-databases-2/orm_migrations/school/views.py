from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    students = Student.objects.prefetch_related('teacher').all()
    # object_list = [{'student': student, 'teachers': student.teacher.all()} for student in students]
    # сначала делал через list comprehensions, потом поменял. Подскажите, как делать лучше?
    context = {
        'object_list': students
    }
    return render(request, template, context)
