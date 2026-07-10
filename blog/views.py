from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
# Create your views here.
class PostView(generic.View):
    def get(self, request):
        return HttpResponse("Hello, World!")
    