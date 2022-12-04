from django.contrib import admin

# Register your models here.

from .models import Movies, Comments, React, Share, Bookmark

admin.site.register(Movies)
admin.site.register(Comments)
admin.site.register(React)
admin.site.register(Share)
admin.site.register(Bookmark)