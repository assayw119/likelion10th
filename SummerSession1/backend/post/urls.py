from django.urls import path
from .views import *

urlpatterns = [
    path('', ListPost, name='ListPost'),
]