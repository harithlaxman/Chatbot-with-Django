from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
# class details(models.Model):
#     email_id = models.EmailField(max_length=254)
#     email_content = models.TextField()
#     email_when = models.DateTimeField()

#     def __str__(self):
#         return self.email_id

class User(AbstractUser):
    pass

class FriendDetails(models.Model):
    friend_name = models.CharField(max_length=255)
    friend_user_name = models.CharField(max_length=255)
    rating = models.IntegerField()
    user = models.ForeignKey(User, default=1, on_delete=models.SET_DEFAULT)
    class Meta:
        verbose_name_plural = "Friend_Details"
    def __str__(self):
        return self.friend_user_name
