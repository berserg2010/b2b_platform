from django.db import models
from datetime import date
from django.contrib.auth import get_user_model


class Order(models.Model):

    # customer = models.ForeignKey(
    #     'Customer',
    #     on_delete=models.CASCADE,
    #     verbose_name='Заказчик',
    # )
    title = models.CharField(
        max_length=300,
        verbose_name='Наименование заказа',
    )
    # category = models.ForeignKey(
    #     'Category',
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     verbose_name='Категория',
    # )
    city_order = models.CharField(
        max_length=50,
        verbose_name='Город',
        blank=True,
        default='',
    )
    budget_order = models.FloatField(
        verbose_name='Бюджет, руб.',
        null=True,
        blank=True,
    )
    expiration_date = models.DateField(
        default=date.today,
        verbose_name='Дата окончания подачи предложений',
    )
    placement_date = models.DateField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )
    last_modified_date = models.DateTimeField(
        auto_now=True,
        verbose_name='Последние изменения',
    )
    requirement = models.CharField(
        max_length=300,
        verbose_name='Особые требования к исполнителю',
        blank=True,
        default='',
    )
    description = models.TextField(
        max_length=5000,
        verbose_name='Описание',
    )
    file_order = models.FileField(
        upload_to='',
        verbose_name='Прикрепить файлы',
        blank=True,
        default='',
    )

    def __str__(self):
        return self.title
