from django.db import models


class Offer(models.Model):

    # title = models.ForeignKey(
    #     'Order',
    #     on_delete=models.CASCADE,
    #     verbose_name='Тендер',
    # )
    # producer = models.ForeignKey(
    #     'Producer',
    #     on_delete=models.CASCADE,
    #     verbose_name='Исполнитель',
    # )
    # customer = models.ForeignKey(
    #     'Customer',
    #     on_delete=models.CASCADE,
    #     verbose_name='Заказчик',
    # )
    price_offer = models.FloatField(
        verbose_name='Предложение, руб.',
    )
    placement_date = models.DateField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )
    last_modified_date = models.DateTimeField(
        auto_now=True,
        verbose_name='Последние изменения',
    )
    description = models.TextField(
        max_length=5000,
        verbose_name='Условия',
    )
    file_offer = models.FileField(
        upload_to='',
        verbose_name='Прикрепить файлы',
        blank=True,
        default=None,
    )

    # Принятие предложения, кнопка в интерфейсе. Если True, то создается объект класса Contract
    # adoption = False

    # def __str__(self):
    #     return f'Исполнитель: {self.producer} / Тендер: {self.title} / Заказчик: {self.customer}'
