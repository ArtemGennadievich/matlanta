from django.contrib import admin
from .models import *


class Comment(admin.StackedInline):
    model = Comments
    fields = ('order_date_add', 'comment_text')
    readonly_fields = ('order_date_add', )
    extra = 0


class VisualAdmOrder(admin.ModelAdmin):
    list_display = (
        'id', 'order_status', 'order_name', 'order_phone', 'order_email', 'order_date', 'order_date_add',
        'order_comment')
    list_display_links = ('id', 'order_name', 'order_phone')
    search_fields = ('order_status', 'order_name', 'order_phone', 'order_date_add')
    list_filter = ('order_status', 'order_date_add')
    list_editable = ('order_status',)
    fields = (
        'order_status', 'order_name', 'order_phone', 'order_email', 'order_date', 'order_date_add')
    readonly_fields = ('order_date', 'order_date_add')
    list_per_page = 5
    list_max_show_all = 50
    inlines = [Comment,]


admin.site.register(Order, VisualAdmOrder)
admin.site.register(StatusCrm)
admin.site.register(Comments)
