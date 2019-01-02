from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class CustomUser(User):

    def __str__(self):
        return self.username

class Profile(models.Model):

	bio = models.TextField(max_length = 255, blank = True, null = True)	
	user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, default="")