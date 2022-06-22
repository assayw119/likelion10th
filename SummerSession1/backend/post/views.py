from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
# Response 추가
from rest_framework.response import Response
# HTTP method를 처리하기 위한 api_view 데코레이터 추가
from rest_framework.decorators import api_view

from .models import Post
# serializers에서 Postserializer를 가져옴
from .serializers import PostSerializer

# 포스트 리스트 뷰
@api_view(['GET'])
def ListPost(request):
    # GET 방식을 받아왔을 때
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(data=serializer.data)
