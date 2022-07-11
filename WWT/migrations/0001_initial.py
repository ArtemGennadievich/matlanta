# Generated by Django 4.0.5 on 2022-06-12 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WWT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_img', models.ImageField(upload_to='car_img/')),
                ('car_title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('car_text', models.CharField(max_length=200, verbose_name='Текст')),
                ('car_status', models.CharField(default='0', max_length=100, null=True, verbose_name='Статус переключателя')),
            ],
            options={
                'verbose_name': 'Слайд',
                'verbose_name_plural': 'Слайды',
            },
        ),
    ]
