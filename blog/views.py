from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from blog.models import Post
# Create your views here.
class PostView(generic.TemplateView):
    template_name = 'blog/index.html'
    
    def get_context_data(self, **kwargs):
        conteudo = super().get_context_data(**kwargs)
        conteudo["post_list"] = Post.objects.all()
        return conteudo
        