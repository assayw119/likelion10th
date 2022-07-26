from xml.dom.minidom import Identified
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import HttpResponse
import json

# introduce view 함수
def showintroduce(request):
    
    return render(request, 'main/introduce.html')

# activities view 함수
def showactivities(request):
    activities = Post.objects.all()
    return render(request, 'main/activities.html', {'activities':activities})

# contact view 함수
def showfavorite(request):
    favorites = Favorite.objects.all()
    return render(request, 'main/favorite.html', {'favorites':favorites})

# contact view 함수
def showcontact(request):
    
    return render(request, 'main/contact.html')

## Activity
def activity_detail(request, id):
    post = get_object_or_404(Post, pk = id)
    all_comments = post.comments.all().order_by('-created_at')
    return render(request, 'main/activity_detail.html', {'post':post, 'comments':all_comments})

def new(request):
    return render(request, 'main/activity_new.html')

def create(request):
    new_acti = Post()
    new_acti.writer = request.user
    new_acti.acti_title = request.POST['acti_title']
    new_acti.acti_insert = request.POST['acti_insert']
    new_acti.acti_date = request.POST['acti_date']
    new_acti.acti_image = request.FILES.get('acti_image')
    new_acti.save()
    return redirect('main:activitydetail', new_acti.id)

def edit(request, id):
    edit_acti = Post.objects.get(id=id)
    return render(request, 'main/activity_edit.html', {'post':edit_acti})

def update(request, id):
    update_acti = Post.objects.get(id=id)
    update_acti.writer = request.user
    update_acti.acti_title = request.POST['acti_title']
    update_acti.acti_insert = request.POST['acti_insert']
    update_acti.acti_date = request.POST['acti_date']
    update_acti.save()
    return redirect('main:activitydetail', update_acti.id)

def delete(request, id):
    delete_acti = Post.objects.get(id=id)
    delete_acti.delete()
    return redirect('main:showactivities')

def create_comment(request, id):
    new_comment = Comment()
    new_comment.writer = request.user
    new_comment.content = request.POST['content']
    new_comment.post = get_object_or_404(Post, pk = id)
    new_comment.save()
    return redirect('main:activitydetail', id)

def edit_comment(request, id):
    comment = Comment.objects.get(id=id)
    if request.user == comment.writer:
        return render(request, 'main/activity_comment_edit.html', {'comment':comment})
    else:
        return redirect('main:activitydetail', comment.post.id)

def delete_comment(request, id):
    comment = Comment.objects.get(id=id)
    if request.user == comment.writer:
        comment.delete()
    return redirect("main:activitydetail", comment.post.id)


def update_comment(request, id):
    comment = Comment.objects.get(id=id)
    comment.content = request.POST.get("content")
    comment.save()
    return redirect("main:activitydetail", comment.post.id)

# like_toggle 함수 작성하기
@require_POST # post 형식의 http 통신
@login_required # login이 되어 있는 상태인 경우
def like_toggle(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    post_like, post_like_created = Like.objects.get_or_create(user=request.user, post=post)

    if not post_like_created:
        post_like.delete()
        result = "like_cancel"
    else:
        result = "like"
    context = {
        "like_count" : post.like_count,
        "result" : result
    }
    return HttpResponse(json.dumps(context), content_type = "application/json")

def dislike_toggle(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    post_like, post_dislike_created = Dislike.objects.get_or_create(user=request.user, post=post)

    if not post_dislike_created:
        post_like.delete()
        result = "dislike_cancel"
    else:
        result = "dislike"
    context = {
        "dislike_count" : post.dislike_count,
        "result" : result
    }
    return HttpResponse(json.dumps(context), content_type = "application/json")

# my_like 함수 작성하기
def my_like(request, user_id):
    user = User.objects.get(id = user_id)
    like_list = Like.objects.filter(user = user)
    context = {
        'like_list' : like_list,
    }
    return render(request, 'items/my_like.html', context)


## Favorite

def favorite_detail(request, id):
    favorite = get_object_or_404(Favorite, pk = id)
    all_comments = favorite.favoritecomments.all().order_by('-created_at')
    return render(request, 'main/favorite_detail.html', {'favorite':favorite, 'comments':all_comments})

def favorite_new(request):
    return render(request, 'main/favorite_new.html')

def favorite_create(request):
    new_favo = Favorite()
    new_favo.writer = request.user
    new_favo.favo_title = request.POST['favo_title']
    new_favo.favo_image = request.FILES.get('favo_image')
    new_favo.save()
    return redirect('main:favorite_detail', new_favo.id)

def favorite_edit(request, id):
    edit_favo = Favorite.objects.get(id=id)
    return render(request, 'main/favorite_edit.html', {'favorite':edit_favo})

def favorite_update(request, id):
    update_favo = Favorite.objects.get(id=id)
    update_favo.writer = request.user
    update_favo.favo_title = request.POST['favo_title']
    update_favo.favo_image = request.FILES.get('favo_image')
    update_favo.save()
    return redirect('main:favorite_detail', update_favo.id)

def favorite_delete(request, id):
    delete_favo = Favorite.objects.get(id=id)
    delete_favo.delete()
    return redirect('main:showfavorite')

def favorite_create_comment(request, id):
    new_comment = FavoriteComment()
    new_comment.writer = request.user
    new_comment.content = request.POST['content']
    new_comment.favorite = get_object_or_404(Favorite, pk = id)
    new_comment.save()
    return redirect('main:favorite_detail', id)


def favorite_edit_comment(request, id):
    comment = FavoriteComment.objects.get(id=id)
    if request.user == comment.writer:
        return render(request, 'main/favorite_comment_edit.html', {'comment':comment})
    else:
        return redirect('main:favorite_detail', comment.favorite.id)

def favorite_delete_comment(request, id):
    comment = FavoriteComment.objects.get(id=id)
    if request.user == comment.writer:
        comment.delete()
    return redirect("main:favorite_detail", comment.favorite.id)


def favorite_update_comment(request, id):
    comment = FavoriteComment.objects.get(id=id)
    comment.content = request.POST.get("content")
    comment.save()
    return redirect("main:favorite_detail", comment.favorite.id)


# like_toggle 함수 작성하기
@require_POST # post 형식의 http 통신
@login_required # login이 되어 있는 상태인 경우
def favorite_like_toggle(request, post_id):
    favorite = get_object_or_404(Favorite, pk = post_id)
    favorite_like, favorite_like_created = FavoriteLike.objects.get_or_create(user=request.user, favorite=favorite)

    if not favorite_like_created:
        favorite_like.delete()
        result = "like_cancel"
    else:
        result = "like"
    context = {
        "like_count" : favorite.like_count,
        "result" : result
    }
    return HttpResponse(json.dumps(context), content_type = "application/json")

def favorite_dislike_toggle(request, post_id):
    favorite = get_object_or_404(Favorite, pk = post_id)
    favorite_dislike, favorite_dislike_created = FavoriteDislike.objects.get_or_create(user=request.user, favorite=favorite)

    if not favorite_dislike_created:
        favorite_dislike.delete()
        result = "dislike_cancel"
    else:
        result = "dislike"
    context = {
        "dislike_count" : favorite.dislike_count,
        "result" : result
    }
    return HttpResponse(json.dumps(context), content_type = "application/json")


# my_like 함수 작성하기
def favorite_my_like(request, user_id):
    user = User.objects.get(id = user_id)
    favorite_like_list = FavoriteLike.objects.filter(user = user)
    context = {
        'like_list' : favorite_like_list,
    }
    return render(request, 'items/favorite_my_like.html', context)

