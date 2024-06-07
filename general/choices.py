from django.db import models


class UserRoleType(models.TextChoices):
    employee = "employee", "Employee"
    client = "client", "Client"
