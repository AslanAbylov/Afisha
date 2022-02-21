from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

    @property
    def count_movie(self):
        return self.movie.all().count()



class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField('')
    duration = models.FloatField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def count_reviews(self):
        return self.reviews.all().count()

    @property
    def rating(self):
        review = Review.objects.filter(movie=self)
        sum = 0
        for i in review:
            sum += i.stars
            return sum/review.count()

    @property
    def all_reviews(self):
        reviews = Review.objects.filter(movie=self)
        return [{'id': i.id, 'text': i.text} for i in reviews]


class Review(models.Model):
    text = models.TextField('')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True)
    stars = models.IntegerField(default=5)

    def __str__(self):
        return self.text

