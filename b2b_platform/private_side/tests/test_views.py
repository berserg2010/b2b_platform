import pytest
from django.urls import reverse


pytestmark = pytest.mark.django_db


def test_get_private_side(client, django_user_model):

    # url = '/private_side/'
    url = reverse('private_side:main')

    username = "user1"
    password = "alakdsjf;asdkfja;df"

    response = client.get(url)
    assert response.status_code == 302

    user = django_user_model(username=username)
    user.set_password(password)
    user.save()
    assert django_user_model.objects.count() > 0

    client.login(username=username, password=password)
    response = client.get(url)
    assert response.status_code == 200
