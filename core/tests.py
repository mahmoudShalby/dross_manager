from django.test import TestCase
from .models import Stage, Grade, Group, Test, Student
from django.contrib.auth.models import User
from random import randint

class CoreTestCase(TestCase):
  def main(self):
    owner = User.objects.create(username='ahmed')
    stage = Stage.objects.create(name='primary', owner=owner)
    grade = Grade.objects.create(stage=stage)
    group = Group.objects.create(grade=grade, classes=24, class_price=10)
    [Student.objects.create(group=group, name=name) for name in ('Ahmed', 'Mohamed', 'Mahmoud')]

    owner = User.objects.get(username='ahmed')
    stage = Stage.objects.get(owner=owner, name='primary')
    grade = Grade.objects.get(stage=stage)
    group = Group.objects.get(grade=grade)
    self.assertEqual(Student.objects.get(group=group, name='Mohamed').name, 'Mohamed')
