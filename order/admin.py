from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = NewGallery


class CategoryAdminSlug(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('cat_order_title',)}


class CategoryAdminSlugGlobal(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('cat_title',)}
    list_display = ('id', 'cat_title', 'slug')
    list_editable = ('cat_title','slug')


class AdminSlugGlobal(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('order_main_title',)}
    list_display = (
        'id', 'order_main_title', 'order_price', 'cat', 'order_is_published', 'get_img', 'order_main_img_mini',
        'order_dop_title1',
        'order_dop_title2',
        'order_dop_title3', 'order_maim_date_add')
    list_editable = ('order_price', 'cat', 'order_is_published', 'order_dop_title1',
                     'order_dop_title2',
                     'order_dop_title3')
    list_display_links = ('order_main_title', 'id')
    list_filter = ('cat', 'order_is_published', 'order_maim_date_add')
    search_fields = ('order_main_title', 'order_price',)
    fields = (
        'order_main_title', 'slug', 'order_price', 'cat', 'order_is_published', 'get_img', 'order_main_img',
        'get_mini_img', 'order_main_img_mini','order_text',
        'order_dop_title1',
        'order_dop_title2',
        'order_dop_title3',
        'order_dop_title4',
        'order_dop_title5',
        'order_dop_title6', 'order_img_2','order_img_3','order_img_4','order_img_5','order_img_6','order_maim_date','order_maim_date_add')
    readonly_fields = ('order_maim_date', 'order_maim_date_add', 'get_img','get_mini_img')



    def get_img(self, obj):
        if obj.order_main_img:
            return mark_safe(f'<img src="{obj.order_main_img.url}" width="200">')
        else:
            return 'Нету изображения'

    def get_mini_img(self, obj):
        if obj.order_main_img_mini:
            return mark_safe(f'<img src="{obj.order_main_img_mini.url}" width="200">')
        else:
            return 'Нету изображения'

    get_img.short_description = 'Главная картинка'


class OrderNewAdmin(admin.ModelAdmin):
    inlines = [GalleryInline, ]


admin.site.register(OrderNew, AdminSlugGlobal)
admin.site.register(NewCategoryOrder, CategoryAdminSlug)
admin.site.register(NewCategory, CategoryAdminSlugGlobal)
admin.site.site_title = 'Админка|Atlanta'
admin.site.site_header = 'Админка|Atlanta'
