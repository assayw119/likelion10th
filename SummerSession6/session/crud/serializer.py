from rest_framework import serializers
from .models import *

class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie', )


class MovieListSerializer(serializers.ModelSerializer):
    comments = ReviewListSerializer(many=True, read_only=True)
    
    class Meta:
        model = Movie
        fields = ('name','content','created_at','updated_at','comments')

