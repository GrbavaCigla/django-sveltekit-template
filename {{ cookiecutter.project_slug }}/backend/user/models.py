from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, UserManager, make_password
from django.conf import settings


class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)



class User(AbstractUser):
    if settings.DELETE_USERNAME:
        REQUIRED_FIELDS = ["first_name", "last_name"]
        USERNAME_FIELD = "email"
        username_validator = None
        username = None

        objects = CustomUserManager()
    else:
        REQUIRED_FIELDS = ["first_name", "last_name", "email"]


User._meta.get_field("email").null = False
User._meta.get_field("email").blank = False
User._meta.get_field("email")._unique = True

User._meta.get_field("first_name").null = False
User._meta.get_field("first_name").blank = False

User._meta.get_field("last_name").null = False
User._meta.get_field("last_name").blank = False


