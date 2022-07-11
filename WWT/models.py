from django.db import models


class WWT(models.Model):
    car_img = models.ImageField(upload_to='car_img/')
    car_title = models.CharField(max_length=200, verbose_name='Заголовок')
    car_text = models.CharField(max_length=200, verbose_name='Текст')
    car_status = models.CharField(max_length=100, null=True, default='0', verbose_name='Статус переключателя')

    def __str__(self):
        return self.car_title

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'
