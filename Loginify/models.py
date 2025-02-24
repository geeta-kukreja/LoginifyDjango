from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class UserDetails(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=12, blank=True)
    
    def save(self, *args, **kwargs):
        # Hash password before saving if it's not already hashed
        if not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
