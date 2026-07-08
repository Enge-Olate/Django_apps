import pytest
from pytest_factoryboy import register

from blog.factories import PostFactory, UserFactory


register(UserFactory)
register(PostFactory)


@pytest.fixture
def django_user_model():
    from django.contrib.auth import get_user_model

    return get_user_model()