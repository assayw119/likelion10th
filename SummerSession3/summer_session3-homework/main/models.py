from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Activity
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    acti_title = models.CharField(max_length=200)
    acti_date = models.CharField(max_length=100)
    acti_insert = models.TextField()
    like_user_set = models.ManyToManyField(User, blank=True, related_name='likes_user_set', through='Like')
    dislike_user_set = models.ManyToManyField(User, blank=True, related_name='dislikes_user_set', through='Dislike')
    
    def __str__(self):
        return self.acti_title
    
    @property
    def like_count(self):
        return self.like_user_set.count()

    @property
    def dislike_count(self):
        return self.dislike_user_set.count()

class Comment(models.Model):
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post ,on_delete=models.CASCADE, related_name ='comments')
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)

#좋아요
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together =(('user', 'post'))

#싫어요
class Dislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('user', 'post'))

##

#Favorite
class Favorite(models.Model):
    id = models.AutoField(primary_key=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    favo_title = models.CharField(max_length=100)
    favo_image = models.ImageField(upload_to = 'favorites/', blank=True, null=True)
    favo_like_user_set = models.ManyToManyField(User, blank=True, related_name='favorite_likes_user_set', through='FavoriteLike')
    favo_dislike_user_set = models.ManyToManyField(User, blank=True, related_name='favorite_dislikes_user_set', through='FavoriteDislike')
    
    @property
    def like_count(self):
        return self.favo_like_user_set.count()
    
    @property
    def dislike_count(self):
        return self.favo_dislike_user_set.count()

class FavoriteComment(models.Model):
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    favorite = models.ForeignKey(Favorite ,on_delete=models.CASCADE, related_name ='favoritecomments')
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)

#좋아요
class FavoriteLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    favorite = models.ForeignKey(Favorite, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together =(('user', 'favorite'))

#싫어요
class FavoriteDislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    favorite = models.ForeignKey(Favorite, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('user', 'favorite'))