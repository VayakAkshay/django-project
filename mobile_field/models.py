from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
# from django.contrib.auth.models import PermissionsMixin
# from django.utils.translation import ugettext_lazy as _

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    otp_field = models.IntegerField(default=0)
    objects = UserManager()
    USERNAME_FIELD =  'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email + "-" + str(self.otp_field)