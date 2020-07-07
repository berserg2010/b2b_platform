from django.db import models
from django.contrib.auth import get_user_model


PRIMARY_ROLE_CHOICES = [
    ('C', 'Customer'),
    ('P', 'Producer'),
]


CLASSIFIER_OF_NATIONAL_ECONOMY_BRANCHES_CHOICES = [
    (10000, 'Промышленность'),
    (20000, 'Сельское хозяйство'),
    (30000, 'Лесное хозяйство'),
    (40000, 'Рыбное хозяйство'),
    (50000, 'Транспорт и связь'),
    (60000, 'Строительство'),
    (70000, 'Торговля и общественное питание'),
    (80000, 'Материально-техническое снабжение и сбыт'),
    (81000, 'Заготовки'),
    (82000, 'Информационно-вычислительное обслуживание'),
    (83000, 'Операции с недвижимым имуществом'),
    (84000, 'Общая коммерческая деятельность по обеспечению функционирования рынка'),
    (85000, 'Геология и разведка недр, геодезическая и гидрометеорологическая службы'),
    (87000, 'Прочие виды деятельности сферы материального производства, которые собираются по двум первым знакам'),
    (90000, 'Жилищно-коммунальное хозяйство'),
    (90300, 'Непроизводственные виды бытового обслуживания населения'),
    (91000, 'Здравоохранение, физическая культура и социальное обеспечение'),
    (92000, 'Народное образование'),
    (93000, 'Культура и искусство'),
    (95000, 'Наука и научное обслуживание'),
    (96000, 'Финансы, кредит, страхование и пенсионное обеспечение'),
    (97000, 'Управление'),
    (98000, 'Общественные объединения'),
    (99000, 'Экстерриториальные организации и органы'),
]


class CustomAuth(models.Model):

    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    tel = models.CharField(
        max_length=12,
        blank=True,
        default='',
    )
    primary_role = models.CharField(
        max_length=1,
        choices=PRIMARY_ROLE_CHOICES,
        default='C'
    )


class CompanyDetails(models.Model):

    classifier = models.PositiveSmallIntegerField(
        choices=CLASSIFIER_OF_NATIONAL_ECONOMY_BRANCHES_CHOICES,
        verbose_name='Наименование категории',
    )

    name_company = models.CharField(
        max_length=100,
        verbose_name='Наименование компании',
    )
    inn = models.CharField(
        max_length=10,
        verbose_name='ИНН',
    )
    kpp = models.CharField(
        max_length=9,
        verbose_name='КПП',
    )
    legal_address = models.CharField(
        max_length=300,
        verbose_name='Юридический адрес',
    )
    actual_address = models.CharField(
        max_length=300,
        verbose_name='Фактический адрес',
        blank=True,
        default='',
    )
