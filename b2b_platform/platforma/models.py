from datetime import date

import self as self
from django.db import models


# Create your models here.


class Customer (models.Model):
    title = models.CharField (max_length=100,
                              verbose_name='Наименование компании')
    inn = models.CharField (max_length=10,
                            verbose_name='ИНН')
    kpp = models.CharField (max_length=9,
                            verbose_name='КПП')
    legal_address = models.CharField (max_length=300,
                                      verbose_name='Юридический адрес')
    actual_address = models.CharField (max_length=300,
                                       verbose_name='Фактический адрес',
                                       blank=True)
    name = models.CharField (max_length=100,
                             verbose_name='Контактное лицо (ФИО)')
    phone = models.CharField (max_length=100,
                              verbose_name='Контактный номер телефона')

    def __str__(self):
        return self.title


class Producer (models.Model):
    title = models.CharField (max_length=100,
                              verbose_name='Наименование компании')
    inn = models.CharField (max_length=10,
                            verbose_name='ИНН')
    kpp = models.CharField (max_length=9,
                            verbose_name='КПП')
    legal_address = models.CharField (max_length=300,
                                      verbose_name='Юридический адрес')
    actual_address = models.CharField (max_length=300,
                                       verbose_name='Фактический адрес',
                                       blank=True)
    name = models.CharField (max_length=100,
                             verbose_name='Контактное лицо (ФИО)')
    phone = models.CharField (max_length=100,
                              verbose_name='Контактный номер телефона')

    def __str__(self):
        return self.title


class Category (models.Model):
    title = models.CharField (max_length=300,
                              verbose_name='Наименование категории')

    def __str__(self):
        return self.title


class Order (models.Model):
    """Заказ конкретного Заказчика"""
    customer = models.ForeignKey ('Customer',
                                  on_delete=models.CASCADE,
                                  verbose_name='Заказчик')
    title = models.CharField (max_length=300,
                              verbose_name='Наименование заказа')
    category = models.ForeignKey ('Category',
                                  on_delete=models.SET_NULL,
                                  null=True,
                                  verbose_name='Категория')
    city_order = models.CharField (max_length=50,
                                    verbose_name='Город',
                                    blank=True)
    budget_order = models.FloatField (verbose_name='Бюджет, руб.',
                                       blank=True)
    expiration_date = models.DateField (default=date.today,
                                        verbose_name='Дата окончания подачи предложений')
    placement_date = models.DateField (auto_now_add=True,
                                       verbose_name='Дата создания')
    last_modified_date = models.DateTimeField (auto_now=True,
                                               verbose_name='Последние изменения')
    requirement = models.CharField (max_length=300,
                                    verbose_name='Особые требования к исполнителю',
                                    blank=True)
    description = models.TextField (max_length=5000,
                                    verbose_name='Описание')
    file_order = models.FileField (upload_to='',
                                    verbose_name='Прикрепить файлы',
                                    blank=True)

    def __str__(self):
        return self.title


class Offer (models.Model):
    """Предложение для конкретного Тендера от конкретного Исполнителя"""
    title = models.ForeignKey ('Order',
                                on_delete=models.CASCADE,
                                verbose_name='Тендер')
    producer = models.ForeignKey('Producer',
                                 on_delete=models.CASCADE,
                                 verbose_name='Исполнитель')
    customer = models.ForeignKey('Customer',
                                 on_delete=models.CASCADE,
                                 verbose_name='Заказчик')
    price_offer = models.FloatField (verbose_name='Предложение, руб.')
    placement_date = models.DateField (auto_now_add=True,
                                       verbose_name='Дата создания')
    last_modified_date = models.DateTimeField (auto_now=True,
                                               verbose_name='Последние изменения')
    description = models.TextField (max_length=5000,
                                    verbose_name='Условия')
    file_offer = models.FileField (upload_to='',
                                    verbose_name='Прикрепить файлы',
                                   blank=True)
    # Принятие предложения, кнопка в интерфейсе. Если True, то создается объект класса Contract
    # adoption = False

    def __str__(self):
        return 'Исполнитель: {0} / Тендер: {1} / Заказчик: {2}'.format(self.producer, self.title, self.customer)


