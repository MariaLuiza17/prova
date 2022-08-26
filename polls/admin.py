from django.contrib import admin

from .models import Question

#http://127.0.0.1:8000/admin/
admin.site.register(Question)