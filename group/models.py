from django.db import models

from django.utils.text import slugify
# Create your models here.

import misaka

from django.contrib.auth import get_user_model

User = get_user_model()

from django import template 
register = template.Library()

class Group(models.Model):
	name = models.CharField(max_length=29,unique=True)
	slug = models.SlugField(allow_unicode=True,unique=True)
	description = models.TextField(black=True,default=' ')
	description_html = models.TextField(editable=False,default=" ",black=True)
	members = models.ManyToManyField(User,through='GroupMember')


	def __str__(self):
		return self.name


	def save(self,*args,**kwargs):
		self.slug = slugify(self.name)
		self.description_html = misaka.html(self.description)
		super().save(*args,**kwargs)

	def get_absolute_url(self):
		return reverse('groups:single',kwargs={'slug':self.slug})



class GroupMember(models.Model):
	group = models.ForeignKey(Group,related_name='memberships')
	user = models.ForeignKey(User,related_name='user_groups')

	def __str__(self):
		return self.user.username

	class Meta:
		unique_together=('group','user')