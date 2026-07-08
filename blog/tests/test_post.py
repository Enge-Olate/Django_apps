import pytest
from django.utils.text import slugify
from blog.models import Post



@pytest.mark.django_db
class TestPostModel:
    def test_create_post_with_factory(self, post_factory):
        post = post_factory()

        assert isinstance(post, Post)
        assert post.title is not None
        assert post.content is not None
        assert post.author is not None
        assert post.status == 1

    def test_post_slug_is_generated_from_title(self, post_factory):
        post = post_factory(title="Meu Primeiro Post")

        assert post.slug == slugify(post.title)

    def test_post_is_saved_with_default_status_draft(self, post_factory):
        post = post_factory(status=0)

        assert post.status == 0

    def test_post_can_be_created_with_user_factory(self, user_factory, post_factory):
        user = user_factory()
        post = post_factory(author=user)

        assert post.author == user
        assert post.author.username == user.username
        
    def test_slug_no_overwritten_if_exists(self, post_factory):
        post = post_factory(title="Django Testing", slug="custom-slug")
        
        assert post.slug == "custom-slug"