from django.test import TestCase
from django.contrib.auth import get_user_model
from .factories import UserFactory, PostFactory
from .models import Post
# Create your tests here.
User = get_user_model()

class TestCreateUser(TestCase):
    def setup(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
    def test_create_user(self):
        user = UserFactory()
        self.assertTrue(user, msg="Usuário criado!")
        
        
class TestCreatePost(TestCase):
    def setup(self):
        pass
    
    def test_create_post(self):
        post_payload = PostFactory.build()
        data ={
            "title" : post_payload.title,
            
        } 
        self.assertEqual(post_payload.title, data["title"])