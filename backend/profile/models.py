from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
# import jwt
# from datetime import datetime,timedelta
# from django.conf import settings
# Create your models here.

# class UserManager(BaseUserManager):
#     use_in_migrations = True
    
#     def create_user(self, login_id, email, password, **kwargs ):
#         if not email:
#             raise ValueError('Users must have an email address')
#         user = self.model(
#             login_id = login_id,
#             email = email,
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
    
#     def create_superuser(self, login_id = None, email = None, password = None ):
#         user = self.create_user(
#             email,
#             password = password,
#             login_id = login_id
#         )
#         user.is_admin = True
#         user.is_superuser = True
#         user.save(using = self._db)
#         return user

# class User(AbstractBaseUser):
#     username = models.CharField(max_length=30, unique=True, null=False, blank=False)
#     email = models.EmailField(max_length=30, unique=True, null=False, blank=False)
#     type = models.CharField(max_length=30)
#     phone = models.IntegerField()
#     created_at = models.DateTimeField(default=timezone.now) 
    
#     is_active = models.BooleanField(default=True)    
#     is_admin = models.BooleanField(default=False)
    
#     objects = UserManager()
    
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email', 'username']
    
#     def __str__(self):
#         return self.login_id
    # @property
    # def token(self):
    #     return self._generate_jwt_token()
    # def _generate_jwt_token(self):
    #     dt = datetime.now() + timedelta(days=60)
    #     token = jwt.encode({
    #         'id':self.pk,
    #         'exp':dt.utcfromtimestamp(dt.timestamp())
    #     },settings.SECRET_KEY, algorithm = 'HS256')
    #     return token
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=30, unique=True, null=False, blank=False)
    email = models.EmailField(max_length=30, unique=True, null=False, blank=False)
    type = models.CharField(max_length=30)
    phone = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now) 
    
class Consumer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.ForeignKey(Profile, related_name="user_consumer", on_delete=models.SET_NULL, null=True)
    customerId = models.TextField()
    point = models.IntegerField() # 매장별
    created_at = models.DateTimeField(default=timezone.now)
    gender = models.CharField(max_length=5)
    
class Store(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.ForeignKey(Profile, related_name="user_store", on_delete=models.SET_NULL, null=True)
    storeId = models.TextField()
    address = models.TextField()
    storename = models.CharField(max_length=50)
    info = models.TextField()
    like = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)

