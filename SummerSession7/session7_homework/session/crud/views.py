from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Movie, Review
from .serializer import MovieListSerializer, ReviewListSerializer
from django.shortcuts import get_list_or_404, render, get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def movie_list_create(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieListSerializer(movies, many=True)

        return Response(data=serializer.data)
    
    if request.method == 'POST':
        serializer = MovieListSerializer(data=request.data)
        #유효성 검사
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data)

@api_view(['GET','PATCH','DELETE'])
@permission_classes([IsAuthenticated])
def movie_detail_update_delete(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    if request.method == 'GET':
        serializer = MovieListSerializer(movie)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = MovieListSerializer(instance=movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
        
    elif request.method == 'DELETE':
        movie.delete()
        data={
            'movie':movie_pk
        }
        return Response(data)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def review_list_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        reviews = Review.objects.filter(movie=movie)
        serializer = ReviewListSerializer(reviews, many=True)

        return Response(data=serializer.data)
    
    if request.method == 'POST':
        serializer = ReviewListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie)
        return Response(data=serializer.data)

@api_view(['GET','PATCH','DELETE'])
@permission_classes([IsAuthenticated])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'GET':
        serializer = ReviewListSerializer(review)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = ReviewListSerializer(instance=review, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
        
    elif request.method == 'DELETE':
        review.delete()
        data={
            'review':review_pk
        }
        return Response(data)

