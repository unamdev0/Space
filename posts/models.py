from django.db import models
from django.urls import reverse
from django.conf import settings

import misaka

from group.models import Group

# Create your models here.

from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
	user = models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now=True)
	message = models.TextField()
	message_html = models.TextField(editable=False,default='')
	group = models.ForeignKey(Group,related_name='posts',null=True,blank=True,on_delete=models.CASCADE)

	def __str__(self):
		return self.message

	def save(self,*args,**kwargs):
		self.message_html = misaka(self.message)
		super().save(*args,**kwargs)

	def get_absolute_url(self):
		return reverse('posts:single',kwargs={'username':self.user.username,'pk':self.pk})

	class Meta:
		unique_together=['user','message']
		ordering = ['-created_at']
        

    	