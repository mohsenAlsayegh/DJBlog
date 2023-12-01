from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializers

@api_view(['GET'])
def post_list_api(request):
    posts = Post.objects.all()
    data = PostSerializers(posts, many=True).data
    return Response({'data' :data})

@api_view(['GET'])
def post_detail_api(request,id):
    posts = Post.objects.get(id=id)
    data = PostSerializers(posts).data
    return Response({'data' :data})

from rest_framework import generics

class PostListAPI(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers

class PostDeatilAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
