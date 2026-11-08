import factory
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from blog.models import Post

User = get_user_model()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username',)

    username = factory.Sequence(lambda n: f"user{n}")
    email = factory.Faker('email')
    password = factory.PostGenerationMethodCall('set_password', '12345')

class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Sequence(lambda n: f"Post {n}")
    author = factory.SubFactory(UserFactory)
    content = factory.Faker("text")
    status = 1
    slug = factory.LazyAttribute(lambda obj: slugify(obj.title))