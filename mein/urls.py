from django.urls import path
from . import views

urlpatterns = [
    path('directors/', views.DirectorListCreateAPIView.as_view()),
    path('directors/<int:id>/', views.DirectorUpdateDeleteAPIView.as_view()),
    path('movies/', views.MovieListCrateAPIView.as_view()),
    path('movies/<int:id>/', views.MovieUpdateDDeleteAPIView.as_view()),
    path('reviews/', views.ReviewListCreateAPIView.as_view()),
    path('reviews/<int:id>/', views.ReviewUpdateDeleteAPIView.as_view()),
    path('register/', views.RegisterAPIView.as_view())
]