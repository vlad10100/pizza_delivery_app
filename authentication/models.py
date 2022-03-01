from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

from django.utils.translation import gettext_lazy as _


from phonenumber_field.modelfields import PhoneNumberField


class CustomUserManager(BaseUserManager):


    #normal user
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("Email should be provided"))

    # email is provided
        email = self.normalize_email(email)                     # normalize_email = lowercasing the domain part
        new_user = self.model(email=email, **extra_fields)      # self.model = CustomUserModel
        new_user.set_password(password)                         # set password = password
        new_user.save()                                         # save password
        return new_user                                         # save user's email and password


    #super user
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        

    # super user must be a staff, active, and superuser
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Superuser must be assigned to is_staff=True"))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("Superuser must be assigned to is_superuser=True"))
        if extra_fields.get('is_active') is not True:
            raise ValueError(_("Superuser must be assigned to is_active=True"))
        return self.create_user(email, password, **extra_fields)




class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=80, unique=True)
    phone_number = PhoneNumberField(blank=True)             #unique=True
    
    USERNAME_FIELD = 'email'                                # instead of username, user will input their email
    REQUIRED_FIELDS = []

    objects = CustomUserManager()                           # Specified that all objects for the class come from the CustomUserManager

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username                                # will display username when called