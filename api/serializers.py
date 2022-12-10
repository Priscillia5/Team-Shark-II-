from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from .models import Movie, Comment, Share, React, Bookmark

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required = True, validators= [UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(validators = [UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(min_length = 8)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        # depth = 1

class MovieSerializer(serializers.ModelSerializer) :
    title = serializers.CharField(required = True)
    url_path = serializers.CharField(required = True)
    description = serializers.CharField(required = True)
    duration = serializers.CharField(required = True)
    
    comments = serializers.PrimaryKeyRelatedField(many = True, queryset = Comment.objects.all())
    reacts = serializers.PrimaryKeyRelatedField(many = True, queryset = React.objects.all())
    shares = serializers.PrimaryKeyRelatedField(many = True, queryset = Share.objects.all())
    bookmarks = serializers.PrimaryKeyRelatedField(many = True, queryset = Bookmark.objects.all())

    class Meta:
        model = Movie
        fields = ('id', 'title', 'url_path', 'description', 'duration', 'comments', 'reacts', 'shares', 'bookmarks')

    def create(self, validated_data):
        movie = Movie.objects.create(**validated_data)
        return movie


class CommentSerializer(serializers.ModelSerializer) :
    text = serializers.CharField(required = True)

    class Meta:
        model = Comment
        fields = ('text', 'user', 'movie')

    def create(self, validated_data):
        comment = Comment.objects.create(**validated_data)
        return comment

class ReactSerializer(serializers.ModelSerializer) :
    class Meta:
        model = React
        fields = '__all__'
        depth = 1

    def create(self, validated_data):
        react = React.objects.create(**validated_data)
        return react

class ShareSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Share
        fields = '__all__'
        depth = 1

    def create(self, validated_data):
        share = Share.objects.create(**validated_data)
        return share

class BookmarkSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Bookmark
        fields = '__all__'
        depth = 1

    def create(self, validated_data):
        bookmark = Bookmark.objects.create(**validated_data)
        return bookmark