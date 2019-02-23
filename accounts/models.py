from django.db import models
from django.contrib import auth

# Create your models here.

class User(auth.models.User,auth.models.PermissionMixin):

	def __str__:
		return "@{}".format(self.username)
		