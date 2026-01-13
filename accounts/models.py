from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    User_picture = models.ImageField(upload_to='User_pictures/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    CHOICES = [
        ('G', 'Guest'),
        ('S', 'Staff'),
        ('M', 'Manager'),
    ]

    user_type = models.CharField(max_length=1, choices=CHOICES, default='G')
    loyalty_points = models.IntegerField(default=0)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return f"{self.username} - ({self.email})"