from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Manager for users"""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        email = email.lower()
        if "@g.bracu.ac.bd" in email or "@bracu.ac.bd" in email:
            user = self.model(
                email=self.normalize_email(email),
                **extra_fields
                )
            user.set_password(password)
            user.save(using=self._db)
            return user
        else:
            raise ValueError("You must input your g-suite email address.")

    def create_superuser(self, email, password):
        """Create super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the System"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'email'
