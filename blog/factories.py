import factory
from django.contrib.auth.models import User
from django.utils.text import slugify
from blog.models import Post


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        skip_postgeneration_save = True

    username = factory.Sequence(lambda n: f"user{n}")
    email = factory.LazyAttribute(lambda obj: f"{obj.username}@example.com")
    password = factory.PostGenerationMethodCall("set_password", "password123")

class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Sequence(lambda n: f"Post {n}")
    author = factory.SubFactory(UserFactory)
    content = factory.Faker("text")
    status = 1
    slug = factory.LazyAttribute(lambda obj: slugify(obj.title))