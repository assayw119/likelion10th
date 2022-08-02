from django.shortcuts import render, get_object_or_404, redirect
from main.models import Post, Favorite
from django.contrib.auth.models import User
# Create your views here.

def mypage(request, id):
    user = get_object_or_404(User, pk=id)

    posts = Post.objects.filter(writer=user)
    favorites = Favorite.objects.filter(writer=user)
    followings = user.profile.followings.all(),

    context = {
        'user':user,
        'posts':posts,
        'favorites':favorites,
        'followings':followings,
    }
    return render(request, 'users/mypage.html', context)

def follow(request, id):
    user=request.user
    followed_user=get_object_or_404(User, pk=id)
    is_follower = user.profile in followed_user.profile.followers.all()
    if is_follower:
        user.profile.followings.remove(followed_user.profile)
    else:
        user.profile.followings.add(followed_user.profile)
    return redirect('users:mypage', followed_user.id)