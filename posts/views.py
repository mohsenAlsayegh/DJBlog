from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import CommentForm, PostForm



#Function Based View

#Post select all object form DB
def post_list(request):
    data = Post.objects.all() 
    context = {
        'object_list' : data 
    }
    return render(request, 'posts/post_list.html',context)


#Post Read from DB (specific page)
def post_detail(request,pk):
    data = Post.objects.get(id=pk)
    comment= Comment.objects.filter(post=data) 
    
    #validation of data
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.post = data
            myform.save()
    else:
        form = CommentForm()

    context = {
        'post': data,
        'comments': comment,
        'form': form
    }
    return render(request, 'posts/post_detail.html',context)


#Creating new post
def create_post(request):
    if request.method  == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.save()
            return redirect('/posts/')
    else:
        form =PostForm()
    
    return render(request, 'posts/post_form.html', {'form':form})


#Editing new post
def edit_post(request,pk):
    post = Post.objects.get(id=pk)

    #data 
    if request.method  == 'POST':
        form = PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.save()
            return redirect('/posts/')
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/post_form.html', {'form':form})


#Delete exsisting post
def delete_post(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('/posts/')
    




