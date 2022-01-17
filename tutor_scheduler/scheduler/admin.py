from django.contrib import admin

from tutor_scheduler.scheduler.models import Issue, Session

# Register your models here.
admin.site.register(Session)
admin.site.register(Issue)
