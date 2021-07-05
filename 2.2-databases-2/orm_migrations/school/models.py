from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    subject = models.CharField(max_length=30, verbose_name='Предмет')

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    group = models.CharField(max_length=30, verbose_name='Класс')
    teacher = models.ManyToManyField(Teacher, through='Group', related_name='students')

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'
        ordering = ['group']

    def __str__(self):
        return self.name


class Group(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teachers_group')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='students_group')
