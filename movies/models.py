from django.db import models
from general.models import BaseModel

# Create your models here.

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