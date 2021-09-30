from django.contrib import admin

# Register your models here.
# Question 5
from .models import Choice, Question

admin.site.register(Choice)
admin.site.register(Question)