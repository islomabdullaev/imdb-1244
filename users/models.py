from django.db import models
from django.contrib.auth.models import AbstractUser



from general.choices import UserRoleType
from general.models import BaseModel
from users.managers import CustomUserManager

# Create your models here.

class User(AbstractUser, BaseModel):
    username = models.CharField(
        max_length=30, unique=False, blank=True, null=True)
    phone = models.CharField(max_length=13, unique=True)
    role = models.CharField(
        max_length=24, choices=UserRoleType.choices,
        default=UserRoleType.client.value)
    date_of_birth = models.DateField(null=True, blank=True)
    bio = models.TextField()
    avatar = models.ImageField(upload_to="users/avatar")

    objects = CustomUserManager()

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["username"]


    def __str__(self) -> str:
        return self.username