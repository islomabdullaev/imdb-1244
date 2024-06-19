# rest framework
from django.db import IntegrityError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle
from rest_framework.filters import SearchFilter

# models
from general.permissions import IsEmployeeOrReadOnly
# from general.throttling import MovieListThrottle
from movies.models import Movie, StreamPlatform

# serializers
from movies.serializers import MovieSerializer, MoviewReviewSerializer, StreamPlatformSerializer

# Create your views here.

class MovieListAPIView(APIView):
    permission_classes = [IsAuthenticated, IsEmployeeOrReadOnly]
    search_fields = ['name']
    filter_backends = [SearchFilter]
    # throttle_classes = [MovieListThrottle]
    def get(self, request):
        search = request.GET.get('search')
        sort = request.GET.get('sort')
        movies = Movie.objects.filter(is_active=True)
        order_by = "created_at"
        if search:
            movies = movies.filter(name__icontains=search)
        if sort:
            match sort:
                case "asc":
                    order_by = "-created_at"
                case "desc":
                    order_by = "created_at"
        movies = movies.order_by(order_by)
        serializer = MovieSerializer(instance=movies, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StreamPlatformListAPIView(APIView):
    def get(self, request):
        streams = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(instance=streams, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieReviewCreateAPIView(APIView):
    def post(self, request):
        serializer = MoviewReviewSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save(user=request.user)
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
            except IntegrityError:
                message = {
                    "message": "Already Created"
                }
                return Response(data=message, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)