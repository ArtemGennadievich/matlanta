from django import template
from order.models import *


register = template.Library()


@register.inclusion_tag('WWT/list_category.html')
def ShowCategory(sort=None, cat_selected=0):
    if not sort:
        cats = NewCategoryOrder.objects.all()
    else:
        cats = NewCategoryOrder.objects.order_by(sort)

    return {'cats': cats, 'cat_selected': cat_selected}
