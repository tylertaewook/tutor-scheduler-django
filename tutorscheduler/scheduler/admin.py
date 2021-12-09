from django.contrib import admin
from .models import Issue, Session


admin.site.register(Session)
admin.site.register(Issue)
# Register your models here.
