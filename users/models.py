from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.


class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, user_name, first_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True.')


        return self.create_user(email, user_name, first_name, password, **other_fields)


    def create_staffuser(self, email, user_name, first_name, password, **other_fields):
        user = self.create_user(email, user_name, first_name, password=password)
        return user

    def create_user(self, email, user_name, first_name, password, **other_fields):
        if not email:
            raise ValueError(_('You must provide an email address'))

        if not password:
            raise ValueError('You must provide a password')


        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, first_name=first_name,  **other_fields)
        user.set_password(password)
        user.save()
        return user

class NewUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=200, unique=True)
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    referral_code = models.CharField(max_length=200, blank=True)
    bitcoin_wallet_address = models.CharField(max_length=200, blank=True)
    phone_number = models.IntegerField()
    next_of_kin = models.CharField(max_length=200, blank=True)
    next_of_kin_phone_number = models.CharField(max_length=200)

    staff = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)


    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']

    def __str__(self):
        return self.user_name


