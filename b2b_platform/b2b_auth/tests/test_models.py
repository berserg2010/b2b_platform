import pytest
from mixer.backend.django import mixer
from django.contrib.auth import get_user_model

from ..models import CustomUser, CompanyDetails


pytestmark = pytest.mark.django_db


def test_create_custom_user():

    tel = '+79876543211'

    custom_user = mixer.blend(
        CustomUser, 
        tel=tel,
    )

    assert custom_user.pk > 0
    assert CustomUser.objects.get(pk=custom_user.pk).tel == tel
    assert get_user_model().objects.get(pk=custom_user.pk).customuser.tel == tel


def test_create_company_detail():

    instance = mixer.blend(CompanyDetails)

    assert instance.pk > 0
