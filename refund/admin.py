from django.contrib import admin
from .models import Refund
# Register your models here.
class RefundAdmin(admin.ModelAdmin):
    class Meta:
        model = Refund
admin.site.register(Refund, RefundAdmin)
