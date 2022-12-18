from django.contrib import admin
from .models import PrivecyPolicy, TermService

# Register your models here.
class PolicyAdmin(admin.ModelAdmin):
    class Meta:
        model = PrivecyPolicy
admin.site.register(PrivecyPolicy, PolicyAdmin)


class TermSerAdmin(admin.ModelAdmin):
    class Meta:
        model = TermService
admin.site.register(TermService, TermSerAdmin)