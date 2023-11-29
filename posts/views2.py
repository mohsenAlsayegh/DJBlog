
from .models import Post
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView


#Class Based View

class Postlist(ListView):   
    model = Post

class PostDetail(DetailView):
    model = Post
  
class AddPost(CreateView):
    model = Post 
    fields = '__all__'
    success_url = '/posts/'

class AddPost(CreateView):
    model = Post 
    fields = '__all__'
    success_url = '/posts/'

class EditPost(UpdateView):
    model = Post 
    fields = '__all__'
    success_url = '/posts/'
    template_name = 'posts/edit.html'

class DeletePost(DeleteView):
    model = Post
    success_url = '/posts/'
