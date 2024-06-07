from django.db import models
from general.models import BaseModel

from users.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
# def validate_rating_value(value):
#     if value >= 1 and value <= 5:
#         return value
#     else:
#         raise ValidationError(message="Value must be between 1 and 5 !")


class StreamPlatform(BaseModel):
    name = models.CharField(max_length=36)
    description = models.TextField()
    url = models.URLField()

    def __str__(self) -> str:
        return self.name


class Movie(BaseModel):
    name = models.CharField(max_length=36)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    stream = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name='movies')

    def __str__(self) -> str:
        return self.name


class MovieReview(BaseModel):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self) -> str:
        return f"{self.movie}|{self.user}: {self.rating}"

    class Meta:
        unique_together = ['movie', 'user']

