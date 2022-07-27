from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Comment
from django.utils import timezone

# Create your views here.

def showmain(request):
    return render(request, 'main/mainpage.html')

def posts(request):
    blogs = Blog.objects.all()
    return render(request, 'main/posts.html', {'blogs': blogs})

def first(request):
    return render(request, 'main/first.html')

def second(request):
    return render(request, 'main/second.html')

def detail(request,id):
    blog = get_object_or_404(Blog, pk =id)
    all_comments = blog.comments.all().order_by('-created_at')
    return render(request,'main/detail.html',{'blog':blog, 'comments':all_comments})

def new(request):
    return render(request,'main/new.html')

def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.writer = request.user
    new_blog.pub_date = timezone.now()
    new_blog.body = request.POST['body']
    new_blog.image = request.FILES.get('image')
    new_blog.save()
    return redirect('main:detail', new_blog.id)

def edit(request, id):
    edit_blog = Blog.objects.get(id=id)
    return render(request, 'main/edit.html', {'blog':edit_blog})

def update(request, id):
    update_blog = Blog.objects.get(id=id)
    update_blog.title = request.POST['title']
    update_blog.writer = request.user
    update_blog.pub_date = timezone.now()
    update_blog.body = request.POST['body']
    update_blog.save()
    return redirect('main:detail', update_blog.id)

def delete(request, id):
    delete_blog = Blog.objects.get(id=id)
    delete_blog.delete()
    return redirect('main:posts')

def create_comment(request, blog_id):
	if request.method == "POST":
		blog = get_object_or_404(Blog, pk=blog_id)
		current_user = request.user
		comment_content = request.POST.get('content')
		Comment.objects.create(content=comment_content, writer=current_user, blog=blog)
	return redirect('main:detail', blog_id)
