from django.shortcuts import render, get_object_or_404
from proj.models import Blog, Circulos, Emails
from proj.forms import EmailForm

from django.views.decorators.csrf import csrf_protect
# Create your views here.

#vista de um post
def post_view(request, post_id):
	blog = get_object_or_404(Blog, id=post_id)
	return render(request, 'post.html', {'blog': blog})


#enviar um email	
@csrf_protect
def post_email(request):
	form = EmailForm(request.POST)
	if form.is_valid():
		form.save()
		return render(request,'contact.html', {})