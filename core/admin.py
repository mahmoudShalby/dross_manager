from django.contrib import admin
from .models import Stage, Grade, Test, Student


for model in (Stage, Grade, Test, Student):
  admin.site.register(model)
