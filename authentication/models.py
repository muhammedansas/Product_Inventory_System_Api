from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,AbstractUser
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        
        if not email:
            raise ValueError("User must have an email Address...!")

        user = self.model(
            email=self.normalize_email(email), username=username, **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password=None):

        user = self.create_user(
            username=username,
            email=email,
            password=password,
        )
        user.is_admin = True
        user.set_password(password)
        user.save(using=self._db)
        return user
    
class User(AbstractBaseUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, verbose_name="email address", unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username
    
    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
