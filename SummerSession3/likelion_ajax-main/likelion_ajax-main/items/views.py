from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required

# 2. 사용할 모듈 불러오기
# 2-1 POST 형식의 HTTP 통신만 받기

# 2-2 response를 변환하는 가장 가본 함수, html 파일, 이미지 등 다양한 응답

# 2-3 딕셔너리를 json 형식으로 바꾸기 위해


def main(request):
    items = Post.objects.all()
    return render(request, 'items/home.html', {'items':items})

def new(request):
    return render(request, 'items/new.html')

def create(request):
    if request.method=="POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        user = request.user
        Post.objects.create(title=title, content=content, image=image,user=user)
    return redirect('main')

def show(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.view_count = post.view_count+1
    post.save()
    return render(request, 'items/show.html', {'post':post})


#삭제하기
def delete(request,post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('main')

# 3. like_toggle 함수 작성하기


# 4. my_like 함수 작성하기
