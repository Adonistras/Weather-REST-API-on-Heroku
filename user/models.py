from django.contrib.auth.models import AbstractUser
from django.db import models

class UserAPI(AbstractUser):
    CHOOSE_GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    gender = models.CharField(max_length=10, choices=CHOOSE_GENDER, verbose_name='Gender', default='Male')

    class Meta:
        ordering = ['-date_joined']



