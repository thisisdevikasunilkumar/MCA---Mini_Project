from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser

# Extend Django default user
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    # Add extra fields if needed
    def __str__(self):
        return self.username
