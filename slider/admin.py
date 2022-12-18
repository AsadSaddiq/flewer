from django.contrib import admin

from slider.models import SliderImages

class SliderAdmin(admin.ModelAdmin):
    class Meta:
        model = SliderImages
admin.site.register(SliderImages, SliderAdmin)