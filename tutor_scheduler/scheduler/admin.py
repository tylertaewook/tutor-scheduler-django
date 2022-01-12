from django.contrib import admin

from .models import Issue, Session

# Register your models here.
admin.site.register(Session)
admin.site.register(Issue)
