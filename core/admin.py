from django.contrib import admin
from .models import Stage, Grade, Group, Test, Student

(admin.site.register(model) for model in (Stage, Grade, Group, Test, Student))
