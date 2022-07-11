from django.db import models


class Main(models.Model):
    main_img = models.ImageField(upload_to='car_img/', verbose_name='Большие картинки', null=True)
    main_mini_img = models.ImageField(upload_to='car_img/mini/', verbose_name='Маленькие картинки', null=True)
    main_title = models.CharField(max_length=200, verbose_name='Название блока')
    maim_date_add = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    maim_date = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def __str__(self):
        return self.main_title

    class Meta:
        verbose_name = 'Блок контент'
        verbose_name_plural = 'Блоки контента'
