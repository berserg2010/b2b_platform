import pytest
from mixer.backend.django import mixer

from ..models import Offer, Order


pytestmark = pytest.mark.django_db


@pytest.fixture(params=[Offer, Order])
def get_models(request):
    return request.param


def test_create_company_detail(get_models):

    instance = mixer.blend(get_models)

    print(instance)

    assert instance.pk > 0
