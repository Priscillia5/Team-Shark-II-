from .models import Movie
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from .serializers import UserSerializer, MovieSerializer, CommentSerializer, ReactSerializer, ShareSerializer, BookmarkSerializer

class HelloView(APIView) :
    """
    Demo Authentication check
    """
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    def get(self, request) :
        content = {'message': 'Hello World!'}
        return Response(content)

class UserEndpoint(APIView) :
    """ 
    Create a user.
    """
    def post(self, request, format = 'json') :
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception = True):
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status = status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MovieEndpoint_1(APIView) :
    """
    Get all saved movies
    """
    def get(self, request, format = 'json') :
        movies = MovieSerializer(Movie.objects.all(), many=True)
        return Response(movies.data, status = status.HTTP_200_OK)

class MovieEndpoint_2(APIView) :
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    """
    Create a new movie
    """
    def post(self, request, format = 'json') :
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception = True) :
            instance = serializer.save(user = request.user)
            if instance :
                movie = MovieSerializer(instance)
                return Response(movie.data, status = status.HTTP_201_CREATED)
            return Response(status = status.HTTP_400_BAD_REQUEST)


class MovieEndpoint_3(APIView) :
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    """
    Get a saved movie
    """
    def get(self, request, movie_id, format = 'json') :
        movie = MovieSerializer(Movie.objects.get(id = movie_id))
        return Response(movie.data)
    
    """
    Update a new movie
    """
    def put(self, request, movie_id, format = 'json', *args, **kwargs) :
        movie = MovieSerializer(Movie.objects.get(id = movie_id), data = request.data)
        if(movie.is_valid(raise_exception = True)) :
            movie.save()
            return Response(movie.data, status = status.HTTP_200_OK)

    """
    Delete a new movie
    """
    def delete(self, request, movie_id, format = 'json', *args, **kwargs) :
        try :
            movie = Movie.objects.get(id = movie_id)
            movie.delete()
            return Response(status = status.HTTP_204_NO_CONTENT)
        except :
            return Response({'error': 'movie with ID not found'}, status = status.HTTP_404_NOT_FOUND)

class CommentEndpoint(APIView) :
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    """
    Create a comment for a movie
    """
    def post(self, request, movie_id, format = 'json') :
        # try :
            movie = Movie.objects.get(id = movie_id)
            serializer = CommentSerializer(data = request.data)
            if serializer.is_valid(raise_exception = True) :
                instance = serializer.save(user = request.user, movie = movie)
                Comment = CommentSerializer(instance)
                return Response(Comment.data, status = status.HTTP_201_CREATED)
        # except :
        #     return Response({'error': 'movie with ID not found'}, status = status.HTTP_404_NOT_FOUND)

class ReactEndpoint(APIView) :
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    """
    Create a reaction for a movie
    """
    def post(self, request, movie_id, format = 'json') :
        try :
            movie = Movie.objects.get(id = movie_id)
            serializer = ReactSerializer(data = request.data)
            if serializer.is_valid(raise_exception = True) :
                instance = serializer.save(user = request.user, movie = movie)
                react = ReactSerializer(instance)
                return Response(react.data, status = status.HTTP_201_CREATED)
        except :
            return Response({'error': 'movie with ID not found'}, status = status.HTTP_404_NOT_FOUND)

class ShareEndpoint(APIView) :
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    """
    Create a share for a movie
    """
    def post(self, request, movie_id, format = 'json') :
        # try :
        movie = Movie.objects.get(id = movie_id)
        serializer = ShareSerializer(data = request.data)
        if serializer.is_valid(raise_exception = True) :
            instance = serializer.save(user = request.user, movie = movie)
            share = ShareSerializer(instance)
            return Response(share.data, status = status.HTTP_201_CREATED)
    # except :
            # return Response({'error': 'movie with ID not found'}, status = status.HTTP_404_NOT_FOUND)

class BookmarkEndpoint(APIView) :
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    """
    Create a bookmark for a movie
    """
    def post(self, request, movie_id, format = 'json') :
        try :
            movie = Movie.objects.get(id = movie_id)
            serializer = BookmarkSerializer(data = request.data)
            if serializer.is_valid(raise_exception = True) :
                instance = serializer.save(user = request.user, movie = movie)
                bookmark = BookmarkSerializer(instance)
                return Response(bookmark.data, status = status.HTTP_201_CREATED)
        except :
            return Response({'error': 'movie with ID not found'}, status = status.HTTP_404_NOT_FOUND)