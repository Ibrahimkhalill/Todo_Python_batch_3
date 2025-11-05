from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.db import transaction
from django.conf import settings
from django.contrib.auth.models import User

class OTP(models.Model):
    email = models.EmailField()
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    attempts = models.IntegerField(default=0)

    def __str__(self):
        return f'OTP for {self.email}: {self.otp}'

    def save(self, *args, **kwargs):
        with transaction.atomic():
            OTP.objects.filter(email=self.email).delete()
            super().save(*args, **kwargs)

    def is_expired(self):
        from django.utils import timezone
        return (timezone.now() - self.created_at).seconds > 120

class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='user_profile'
    )
    
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profile", blank=True, null=True)
    joined_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.user.email if self.user else "No User"