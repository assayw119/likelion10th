from django.urls import path
from .views import *

app_name = 'users'
urlpatterns = [
    path('<int:id>/mypage/', mypage, name='mypage'),
    path('<int:id>/follow', follow, name='follow'),
]