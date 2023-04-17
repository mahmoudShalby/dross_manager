from django.test import TestCase
from .models import Stage, Grade, Group, Test, Student
from django.contrib.auth.models import User
from random import randint

class StageTestCase(TestCase):
  def setup(self):
    owner = User.objects.get(username='admin')
    stage = Stage.objects.create(owner=owner, from_age=7, name='prim')
    grades = (Grade.objects.create(stage=stage, index_in_stage=index+1) for index in range(6))
    groups = (Group.objects.create(grade=grades[index], classes=24, class_price=10) for index in range(6))
    students = []
    for grade_index in range(6):
      for _ in range(10):
        students.append(Student.objects.create(group=groups[grade_index], name=(('Ahmed', 'Mohamed', 'Mahmoud')[randint(0, 2)])))
