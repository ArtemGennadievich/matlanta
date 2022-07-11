from django.db import models
from django.urls import reverse


class OrderNew(models.Model):
    order_main_img = models.ImageField(upload_to='car_img_order/%Y/%m/%d/', verbose_name='Главная картинка')
    order_main_img_mini = models.ImageField(upload_to='car_img_order/%Y/%m/%d/', verbose_name='Картинка брэнда',
                                            null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name='URL')
    order_main_title = models.CharField(max_length=250, verbose_name='Название товара')
    order_dop_title1 = models.CharField(max_length=400, verbose_name='Доп-характеристика1', blank=True)
    order_dop_title2 = models.CharField(max_length=400, verbose_name='Доп-характеристика2', blank=True)
    order_dop_title3 = models.CharField(max_length=400, verbose_name='Доп-характеристика3', blank=True)
    order_dop_title4 = models.CharField(max_length=400, verbose_name='Доп-характеристика4', blank=True)
    order_dop_title5 = models.CharField(max_length=400, verbose_name='Доп-характеристика5', blank=True)
    order_dop_title6 = models.CharField(max_length=400, verbose_name='Доп-характеристика6', blank=True)
    order_img_2 = models.ImageField(upload_to='car_img_order/%Y/%m/%d/', verbose_name='Вторая картинка',
                                    null=True, blank=True)
    order_img_3 = models.ImageField(upload_to='car_img_order/%Y/%m/%d/', verbose_name='Третья картинка',
                                    null=True, blank=True)
    order_img_4 = models.ImageField(upload_to='car_img_order/%Y/%m/%d/', verbose_name='Четвёртая картинка',
                                    null=True, blank=True)
    order_img_5 = models.ImageField(upload_to='car_img_order/%Y/%m/%d/', verbose_name='Пятая картинка',
                                    null=True, blank=True)
    order_img_6 = models.ImageField(upload_to='car_img_order/%Y/%m/%d/', verbose_name='Шестая картинка',
                                    null=True, blank=True
                                    )
    cat = models.ForeignKey('NewCategoryOrder', on_delete=models.PROTECT, verbose_name='Категория')
    order_price = models.CharField(max_length=50, verbose_name='Цена товара')
    order_text = models.TextField(verbose_name='Описание')
    order_maim_date_add = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    order_maim_date = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    order_is_published = models.BooleanField(default=True, verbose_name='Статус Опубликован/Не опубликован')

    def __str__(self):
        return self.order_main_title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = "карточку товара"
        verbose_name_plural = "карточки товара"
        ordering = ['-order_maim_date_add']


class NewCategoryOrder(models.Model):
    cat_order_title = models.CharField(max_length=200, verbose_name='Название категории')
    cat_order_fk = models.ForeignKey('NewCategory', on_delete=models.PROTECT)
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.cat_order_title

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = "подкатегорию"
        verbose_name_plural = "подкатегории"


class NewCategory(models.Model):
    cat_title = models.CharField(max_length=200, verbose_name='Название главной категории')
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.cat_title

    class Meta:
        verbose_name = "категорию"
        verbose_name_plural = "категории"


class NewGallery(models.Model):
    image = models.ImageField(upload_to='gallery/%Y/%m/%d/', blank=True, verbose_name="Дополнительные фотографии")
    product = models.ForeignKey(OrderNew, on_delete=models.CASCADE, related_name='images')
