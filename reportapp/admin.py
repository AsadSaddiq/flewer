from django.contrib import admin
from .models import Report

class ReportAdmin(admin.ModelAdmin):
    class Meta:
        model = Report
admin.site.register(Report, ReportAdmin)
