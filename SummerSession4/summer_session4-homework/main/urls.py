from django.urls import path, include
from .views import *

app_name = 'main'
urlpatterns = [
    # introduce page URL 연결하기 with 별명사용
    path('', showintroduce, name="showintroduce"),

    # activities page URL 연결하기 with 별명사용
    path('activities/', showactivities, name="showactivities"),

    path('activities/<int:id>/', activity_detail, name='activitydetail'),
    path('new/', new, name='new'),
    path('create/', create, name='create'),
    path('edit/<int:id>', edit, name='edit'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),

    path('<str:id>/create_comment', create_comment, name='create_comment'),
    path('<str:id>/edit_comment', edit_comment, name='edit_comment'),
    path('<str:id>/update_comment', update_comment, name='update_comment'),
    path('<str:id>/delete_comment', delete_comment, name='delete_comment'),

    path('like_toggle/<int:post_id>/', like_toggle, name="like_toggle"),
    path('dislike_toggle/<int:post_id>/', dislike_toggle, name="dislike_toggle"),
    path('my_like/<int:user_id>/', my_like, name='my_like'),

    # favorite page URL 연결하기 with 별명사용
    path('favorite/', showfavorite, name="showfavorite"),
    path('favorite/<int:id>/', favorite_detail, name='favorite_detail'),
    path('favorite_new/', favorite_new, name='favorite_new'),
    path('favorite_create/', favorite_create, name='favorite_create'),
    path('favorite_edit/<int:id>', favorite_edit, name='favorite_edit'),
    path('favorite_update/<int:id>', favorite_update, name='favorite_update'),
    path('favorite_delete/<int:id>', favorite_delete, name='favorite_delete'),

    path('<str:id>/favorite_create_comment', favorite_create_comment, name='favorite_create_comment'),
    path('<str:id>/favorite_edit_comment', favorite_edit_comment, name='favorite_edit_comment'),
    path('<str:id>/favorite_update_comment', favorite_update_comment, name='favorite_update_comment'),
    path('<str:id>/favorite_delete_comment', favorite_delete_comment, name='favorite_delete_comment'),

    path('favorite_like_toggle/<int:post_id>/', favorite_like_toggle, name="favorite_like_toggle"),
    path('favorite_my_like/<int:user_id>/', favorite_my_like, name='favorite_my_like'),

    path('favorite_like_toggle/<int:post_id>/', favorite_like_toggle, name="favorite_like_toggle"),
    path('favorite_dislike_toggle/<int:post_id>/', favorite_dislike_toggle, name="favorite_dislike_toggle"),
    path('favorite_my_like/<int:user_id>/', favorite_my_like, name='favorite_my_like'),

    # contact page URL 연결하기 with 별명사용
    path('contact/', showcontact, name="showcontact"),

    
]