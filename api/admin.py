from django.contrib import admin

# Register your models here.

from .models import Movie, Comment, React, Share, Bookmark

admin.site.register(Movie)
admin.site.register(Comment)
admin.site.register(React)
admin.site.register(Share)
admin.site.register(Bookmark)