from django.contrib import admin

from .models import Student, Teacher, Group


class GroupInline(admin.TabularInline):
    model = Group
    extra = 1


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    inlines = (GroupInline,)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = (GroupInline,)
