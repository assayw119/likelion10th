from django.urls import path
from . import views

app_name="items"
urlpatterns = [
    path('', views.main, name="main"),
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
    path('show/<int:post_id>/', views.show, name="show"),
    path('delete/<int:post_id>/', views.delete, name="delete"),
    # 1. like_toggle url 연결하기
    
    # 2. my_like url 연결하기
    
]
