# Generated by Django 4.0.5 on 2022-06-12 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_comment',
            field=models.TextField(null=True, verbose_name='Комментарий'),
        ),
    ]
