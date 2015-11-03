from django.shortcuts import render, get_object_or_404
from proj.models import Blog, Circulos
# Create your views here.
def post_view(request, post_id):
	blog = get_object_or_404(Blog, id=post_id)
	return render(request, 'post.html', {'blog': blog})