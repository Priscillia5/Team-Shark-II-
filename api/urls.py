from . import views
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.HelloView.as_view()),
    path('auth/register', views.UserEndpoint.as_view()),
    path('auth/login', obtain_auth_token, name='api_token_auth'),

    path('movies', views.MovieEndpoint_1.as_view()),
    path('movies', views.MovieEndpoint_2.as_view()),
    path('movies/<int:movie_id>', views.MovieEndpoint_3.as_view()),

    path('movies/<int:movie_id>/comments', views.CommentEndpoint.as_view()),
    path('movies/<int:movie_id>/reacts', views.ReactEndpoint.as_view()),
    path('movies/<int:movie_id>/shares', views.ShareEndpoint.as_view()),
    path('movies/<int:movie_id>/bookmarks', views.BookmarkEndpoint.as_view()),

    # path('react/', views.react, name='React'),
    # path('share/', views.share, name='Share'),
    # path('bookmark/', views.bookmark, name='Bookmark'),
]