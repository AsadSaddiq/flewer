from django.contrib import admin

from payment.models import PaymentHistory

# Register your models here.

class RoomAdmin(admin.ModelAdmin):
    class Meta:
        model = PaymentHistory
admin.site.register(PaymentHistory, RoomAdmin)