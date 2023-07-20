from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from rest_framework.exceptions import ValidationError


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    image = models.ImageField(upload_to='users/', verbose_name='Фотография профиля', blank=True, null=True)
    first_name = models.CharField(max_length=60, verbose_name='Имя')
    last_name = models.CharField(max_length=60, verbose_name='Фамилия')
    email = models.EmailField(unique=True, verbose_name='Почта')
    tel = PhoneNumberField(verbose_name='Номер телефона')
    vk_link = models.URLField(verbose_name='ВК', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'vk_link']

    objects = CustomUserManager()

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Добавьте related_name для поля groups
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='customuser'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Добавьте related_name для поля user_permissions
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
        related_query_name='customuser'
    )

    def clean(self):
        if self.first_name == "":
            raise ValidationError("Введите имя")
        if self.last_name == "":
            raise ValidationError("Введите фамилию")

    def __str__(self):
        return self.first_name + " " + self.last_name
