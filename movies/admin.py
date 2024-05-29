from django.contrib import admin

# models
from movies.models import StreamPlatform, Movie, MovieReview

# Register your models here.

admin.site.register(StreamPlatform)
admin.site.register(Movie)
admin.site.register(MovieReview)