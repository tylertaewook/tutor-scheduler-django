from django.contrib import admin
from .models import Issue, Session, Teacher


admin.site.register(Session)
admin.site.register(Issue)
admin.site.register(Teacher)
# Register your models here.
