# Note: ListView is used to get all the post records
#       while DetailView is used to get just one record
#       from the database.

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
