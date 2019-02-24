from django.views.generic.base import TemplateView


class HomePage(TemplateView):
	template_name = 'index.html'

class test(TemplateView):
	template_name='test.html'

class thankyou(TemplateView):
	template_name='thankyou.html'
