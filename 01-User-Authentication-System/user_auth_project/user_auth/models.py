from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Login(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    login_time = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(null=True, blank=True)  # for browser/device info

    def __str__(self):
        return f"{self.user.username} logged in at {self.login_time}"