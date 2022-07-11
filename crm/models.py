from django.db import models


class StatusCrm(models.Model):
    status_name = models.CharField(max_length=200, verbose_name='Название статуса')

    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Order(models.Model):
    order_name = models.CharField(max_length=200, verbose_name='Имя')
    order_phone = models.CharField(max_length=200, verbose_name='Телефон')
    order_email = models.EmailField(max_length=200, verbose_name='Тип заказа')
    order_comment = models.TextField(verbose_name='Комментарий', null=True)
    order_status = models.ForeignKey(StatusCrm, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Статус')
    order_date_add = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    order_date = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Comments(models.Model):
    comment_request = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')
    comment_text = models.TextField(verbose_name='Текст комментария')
    order_date_add = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    order_date = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def __str__(self):
        return self.comment_text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
