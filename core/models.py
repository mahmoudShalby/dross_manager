from django.db import models
from django.contrib.auth.models import User


class namedLevel(models.Model):
  name = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  class Meta:
    abstract = True
    managed = False

class Stage(namedLevel):
  owner = models.ForeignKey(User, models.CASCADE)
  from_age = models.PositiveSmallIntegerField()

class Grade(namedLevel):
  stage = models.ForeignKey('Stage', models.CASCADE)

class Group(namedLevel):
  stage = models.ForeignKey('Grade', models.CASCADE)
  classes = models.PositiveSmallIntegerField(default=0)
  class_price = models.PositiveSmallIntegerField()

class Test(namedLevel):
  class Level(models.TextChoices):
    ANY = 'A'
    EASE = 'E'
    MIDDLE = 'M'
    Hard = 'H'

  max_mark = models.PositiveSmallIntegerField()
  level = models.CharField(max_length=1, choices=Level.choices, default=Level.ANY)
  created_at = models.DateTimeField(auto_now=True)
  takers = models.ManyToManyField('Student')

  class Meta:
    ordering = ['created_at']

class Student(namedLevel):
  class Level(models.TextChoices):
    NORMAL = 'N'
    INTERMEDIATE = 'I'
    ADVANCED = 'A'

  group = models.ForeignKey('Group', models.CASCADE)
  has_to_pay = models.PositiveSmallIntegerField(default=0)
  paid = models.PositiveSmallIntegerField(default=0)
  attendance = models.PositiveSmallIntegerField(default=0)
  should_pay = models.BooleanField(default=True)
  level = models.TextField(max_length=1, choices=Level.choices, default=Level.NORMAL)

  class Meta:
    ordering = ['name']