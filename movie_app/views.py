from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.serializers import DirectorSerializer
from movie_app.models import Director, Movie, Review
from movie_app.serializers import MovieSerializer
from movie_app.serializers import ReviewSerializer

@api_view(['GET'])
def director_list_view(request):
    directors = Director.objects.all()
    data = DirectorSerializer(directors, many=True).data
    return Response(data=data)

@api_view(['GET'])
def director_detail_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=404, data={'message': 'Director not found'})
    data = DirectorSerializer(director).data
    return Response(data=data)

@api_view(['GET'])
def movie_list_view(request):
    movies = Movie.objects.all()
    data = MovieSerializer(movies, many=True).data
    return Response(data=data)

@api_view(["GET"])
def movie_detail_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=404, data={'massage': 'Movie not found'})
    data = MovieSerializer(movie).data
    return Response(data=data)


@api_view(['GET'])
def reviews_list_view(request):
    reviews = Review.objects.all()
    data = ReviewSerializer(reviews, many=True).data
    return Response(data=data)


@api_view(['GET'])
def review_detail_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=404, data={'massage': 'Review not found'})
    data = ReviewSerializer(review).data
    return Response(data=data)