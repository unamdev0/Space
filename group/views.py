from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin,PermissionReuqiredMixin
from django.contrib import messages
from django.urls import reverse

from django.views import generic
from django.shortcuts import get_object_or_404
from group.models import Group

# Create your views here.

 
class CreateGroup(LoginRequiredMixin,generic.CreateView):
	fields = ('name','description')
	model = Group


class SingleGroup(generic.DetailView):
	model = Group

class ListGroups(generic.ListView):
	model = Group

class JoinGroup(LoginRequiredMixin,generic.RedirectView):

	def get_redirect_url(self,*args,**kwargs):
		return revese ('groups:single',kwargs={'slug':self.kwargs.get('slug')})

	def get(self,request,*args,**kwargs):
		group = get_object_or_404(Group,slug=self.kwargs.get('slug'))

		try:
			GroupMember.objects.create(user=self.request.user,group=group)

		except IntegrityError:
			messages.warning(self.request,("You are already a member"))
		else:
			messages.success(self.request,"You are now a member")

		return super().get(request,*args,**kwargs)

class LeaveGroup(LoginRequiredMixin,generic.RedirectView):

	def get_redirect_url(self,*args,**kwargs):
		return revese ('groups:single',kwargs={'slug':self.kwargs.get('slug')})

	def get(self,request,*args,**kwargs):

		try:
			membership = models.GroupMember.objects.filter(
				user = self.request.user,
				group__slug = self.kwargs,get('slug')).get()

		except:
			message.warning(self.request,"You are not part of this group")
		else:
			membership.delete()
			message.success(self.request,"You have left this group")
		return super().get(request,*args,**kwargs)