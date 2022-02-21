from rest_framework import serializers
from movie_app.models import Director, Movie, Review


class DirectorSerializer(serializers.ModelSerializer):
    movie = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = 'name movie count_movie'.split()

    def get_movie(self, director):
        return director.name

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    director = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = 'title description duration director reviews count_reviews all_reviews rating'.split()

    def get_director(self, movie ):
        try:
            return movie.director.name
        except:
            return 'No director'

    def get_reviews(self, movie):
        serializer = ReviewSerializer(Review.objects.filter(movie=movie), many=True)
        return serializer.data

class MovieReviewSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = 'title rating reviews'.split()

    def get_reviews(self, movie):
        serializer = ReviewSerializer(Review.objects.filter(movie=movie), many=True)
        return serializer.data


