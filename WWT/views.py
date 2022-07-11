from django.shortcuts import render
from .models import WWT
from main_content.models import *
from crm.models import Order
from crm.form import OrderForm
from telegram_bot.Telegram_request import RequestTelegram
from django.views.generic import ListView, DetailView
from order.models import *


def wwt_def(request):
    all_content = Main.objects.all()
    content_img1 = all_content[0].main_img.url
    content_img_mini1 = all_content[0].main_mini_img.url
    content_title1 = all_content[0].main_title
    content_img2 = all_content[1].main_img.url
    content_img_mini2 = all_content[1].main_mini_img.url
    content_title2 = all_content[1].main_title
    content_img3 = all_content[2].main_img.url
    content_img_mini3 = all_content[2].main_mini_img.url
    content_title3 = all_content[2].main_title
    content_img4 = all_content[3].main_img.url
    content_img_mini4 = all_content[3].main_mini_img.url
    content_title4 = all_content[3].main_title
    content_img5 = all_content[4].main_img.url
    content_img_mini5 = all_content[4].main_mini_img.url
    content_title5 = all_content[4].main_title
    content_img6 = all_content[5].main_img.url
    content_img_mini6 = all_content[5].main_mini_img.url
    content_title6 = all_content[5].main_title
    content_img7 = all_content[6].main_img.url
    content_img_mini7 = all_content[6].main_mini_img.url
    content_title7 = all_content[6].main_title
    content_img8 = all_content[7].main_img.url
    content_img_mini8 = all_content[7].main_mini_img.url
    content_title8 = all_content[7].main_title
    car_list_all = WWT.objects.all()
    form_product = OrderForm()
    car_img1 = car_list_all[0].car_img.url
    car_img2 = car_list_all[1].car_img.url
    car_img3 = car_list_all[2].car_img.url
    car_img4 = car_list_all[3].car_img.url
    car_img5 = car_list_all[4].car_img.url
    car_title1 = car_list_all[0].car_title
    car_title2 = car_list_all[1].car_title
    car_title3 = car_list_all[2].car_title
    car_title4 = car_list_all[3].car_title
    car_title5 = car_list_all[4].car_title
    content_list = {
        'content_img1': content_img1,
        'content_title1': content_title1,
        'content_img_mini1': content_img_mini1,
        'content_img2': content_img2,
        'content_title2': content_title2,
        'content_img_mini2': content_img_mini2,
        'content_img3': content_img3,
        'content_title3': content_title3,
        'content_img_mini3': content_img_mini3,
        'content_img4': content_img4,
        'content_title4': content_title4,
        'content_img_mini4': content_img_mini4,
        'content_img5': content_img5,
        'content_title5': content_title5,
        'content_img_mini5': content_img_mini5,
        'content_img6': content_img6,
        'content_title6': content_title6,
        'content_img_mini6': content_img_mini6,
        'content_img7': content_img7,
        'content_title7': content_title7,
        'content_img_mini7': content_img_mini7,
        'content_img8': content_img8,
        'content_title8': content_title8,
        'content_img_mini8': content_img_mini8,
    }
    car_list = {
        'car_img1': car_img1,
        'car_img2': car_img2,
        'car_img3': car_img3,
        'car_img4': car_img4,
        'car_img5': car_img5,
        'car_title1': car_title1,
        'car_title2': car_title2,
        'car_title3': car_title3,
        'car_title4': car_title4,
        'car_title5': car_title5,
        'content_list': content_list,
        'form_product': form_product,
    }
    return render(request, 'WWT/main.html', {'car_list': car_list})


def thank_after_form(request):
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        comment = request.POST['comment']
        save_model = Order(order_name=name, order_phone=phone, order_email=email, order_comment=comment)
        save_model.save()
        RequestTelegram(tg_name=name, tg_phone=phone, tg_email=email, tg_comment=comment)
        return render(request, 'WWT/form_tanks.html', {'name': name})
    else:
        return render(request, 'WWT/form_tanks.html')


menu = [
    {'title': 'Каталог', 'url_name': 'catalog'},
    {'title': 'Главная', 'url_name': 'home_page'},
]
form_product = OrderForm()


class Catalog(ListView):
    model = OrderNew
    template_name = 'WWT/catalog.html'
    context_object_name = 'ord_new'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Каталог'
        context['cat_selected'] = 0
        context['menu'] = menu
        context['form_product'] = form_product
        return context

    def get_queryset(self):
        return OrderNew.objects.filter(order_is_published=True).select_related('cat')


class ShowPost(DetailView):
    model = OrderNew
    template_name = 'WWT/order.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_product'] = form_product
        return context


class ShowForm(ListView):
    model = OrderNew
    template_name = 'WWW/form2'
    context_object_name = 'form'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_product'] = form_product
        return context


class CatalogCategory(ListView):
    model = OrderNew
    template_name = 'WWT/catalog.html'
    context_object_name = 'ord_new'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['ord_new'][0].cat)
        context['cat_selected'] = context['ord_new'][0].cat_id
        context['menu'] = menu
        context['form_product'] = form_product
        return context

    def get_queryset(self):
        return OrderNew.objects.filter(cat__slug=self.kwargs['cat_slug'],
                                       order_is_published=True).select_related(
            'cat')


def About_me(request):
    return render(request, 'WWT/about_me.html')


def delivery(request):
    return render(request, 'WWT/delivery.html')
