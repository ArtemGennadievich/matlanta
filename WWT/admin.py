from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import WWT


class WWTVisual(admin.ModelAdmin):
    list_display = ('car_title', 'car_text', 'get_img')
    list_display_links = ('car_title', 'car_text')
    fields = ('car_title', 'car_text', 'get_img', 'car_status', 'car_img')
    readonly_fields = ('get_img',)


    def get_img(self, obj):
        if obj.car_img:
            return mark_safe(f'<img src="{obj.car_img.url}" width="200">')
        else:
            return 'Нету изображения'

    get_img.short_description = 'Миниатюра'




admin.site.register(WWT, WWTVisual)
