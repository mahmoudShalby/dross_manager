from django.db import models
from django.contrib.auth.models import User

class Stage(models.Model):
  name = models.CharField(max_length=20)
  owner = models.ForeignKey(User, models.CASCADE)

  def __str__(self):
    return self.name

class Grade(models.Model):
  name = models.CharField(max_length=20)
  stage = models.ForeignKey(Stage, models.CASCADE)

  def __str__(self):
    return self.name

class Group(models.Model):
  name = models.CharField(max_length=20)
  grade = models.ForeignKey(Grade, models.CASCADE)
  classes = models.PositiveSmallIntegerField(default=0)
  class_price = models.PositiveSmallIntegerField()

  def __str__(self):
    return self.name

class Test(models.Model):
  class Level(models.TextChoices):
    ANY = 'A'
    EASE = 'E'
    MIDDLE = 'M'
    Hard = 'H'

  name = models.CharField(max_length=20)
  max_mark = models.PositiveSmallIntegerField()
  level = models.CharField(max_length=1, choices=Level.choices, default=Level.ANY)
  takers = models.ManyToManyField('Group')
  created_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name

  class Meta:
    ordering = ['created_at']

class Student(models.Model):
  class Level(models.TextChoices):
    NORMAL = 'N'
    INTERMEDIATE = 'I'
    ADVANCED = 'A'

  name = models.CharField(max_length=20)
  group = models.ForeignKey(Group, models.CASCADE)
  egp = models.PositiveSmallIntegerField(default=0)
  paid = models.PositiveSmallIntegerField(default=0)
  attendance = models.PositiveSmallIntegerField(default=0)
  have_to_pay = models.BooleanField(default=True)
  level = models.TextField(max_length=1, choices=Level.choices, default=Level.NORMAL)

  def __str__(self):
    return self.name

  class Meta:
    ordering = ['name']
