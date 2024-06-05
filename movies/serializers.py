from rest_framework import serializers

from movies.models import Movie, MovieReview, StreamPlatform

from django.utils import timezone


class MovieSerializer(serializers.ModelSerializer):
    time_since = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = "__all__"
    
    def get_time_since(self, object):
        diff = (timezone.now() - object.created_at)
        duration = diff.total_seconds() / 3600
        return round(duration)

class StreamPlatformSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True, read_only=True)
    class Meta:
        model = StreamPlatform
        exclude = ('updated_at', 'created_at', )


class MoviewReviewSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField()
    class Meta:
        model = MovieReview
        exclude = ('updated_at', 'created_at', 'user')
