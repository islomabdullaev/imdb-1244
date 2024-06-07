from django.db import models
from django.contrib.auth.models import AbstractUser

from phone_field import PhoneField

from general.choices import UserRoleType
from general.models import BaseModel

# Create your models here.

class User(AbstractUser, BaseModel):
    username = models.CharField(
        max_length=30, unique=False, blank=True, null=True)
    phone = PhoneField(blank=True, help_text='Contact phone number', unique=True)
    role = models.CharField(
        max_length=24, choices=UserRoleType.choices,
        default=UserRoleType.client.value)
    date_of_birth = models.DateField(null=True, blank=True)
    bio = models.TextField()
    avatar = models.ImageField(upload_to="users/avatar")

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["username"]


    def __str__(self) -> str:
        return self.username