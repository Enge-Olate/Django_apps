import pytest
from django.contrib.auth.models import User

@pytest.mark.django_db
class TestUserModel:
    def test_create_user_with_factory(self, user_factory):
        user = user_factory()

        assert isinstance(user, User)
        assert user.username is not None
        assert user.email.endswith('@example.com')
        
    def test_user_password_is_hashed(self, user_factory):
        user = user_factory(password="password123")

        assert user.check_password("password123") is True
        assert user.password != "password123"  