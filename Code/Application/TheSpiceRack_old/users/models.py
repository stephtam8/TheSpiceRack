from django.db import models
#from django.contrib.auth.models import User

# Create your models here.
class CustomUser():
    full_name = models.CharField(blank=False, max_length=255, default='Noname Jones')
    email = models.EmailField('email address', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return self.full_name