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
	# friend = models.ManyToManyField(FriendDetails, blank=True)
	# friend = models.ForeignKey(FriendDetails, default=1, on_delete=models.SET_DEFAULT)
	pass

class FriendDetails(models.Model):
    friend_name = models.CharField(max_length=255)
    friend_user_name = models.CharField(max_length=255)
    rating = models.IntegerField()
    stars = models.CharField(max_length=255, default="no stars")
    user = models.ManyToManyField(User, blank=True)
    class Meta:
        verbose_name_plural = "Friend_Details"
    def __str__(self):
        return self.friend_user_name