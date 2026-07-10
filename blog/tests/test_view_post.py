import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_view_post(client):
    url = reverse('home')
    response = client.get(url)
    assert response.status_code == 200
    assert b"Hello, World!" in response.content