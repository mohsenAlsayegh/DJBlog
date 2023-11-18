from django.shortcuts import render
from .models import Post
from .forms import PostForm
# Create your views here.

def post_list(request):
    data = Post.objects.all() 
    context = {
        'mohsen' : data 
    }
    return render(request, 'posts/post_list.html',context)

def post_detail(request,post_id):
    data = Post.objects.get(id=post_id)

    context = {
        'post': data 
    }

    return render(request, 'posts/post_detail.html',context)

def create_post(request):
    if request.method  == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form =PostForm()
    
    form = PostForm()
    return render(request, 'posts/new.html', {'form':form})







from django.views.generic import ListView, DetailView

class Postlist(ListView):   
    model = Post

class PostDetail(DetailView):
    model = Post
  
