from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from proj.models import Blog

urlpatterns = patterns('', 
	url(r'^$', ListView.as_view(
		queryset=Blog.objects.all().order_by("-date")[:25],
		template_name="base.html")),

	 url(r'^blog/$', ListView.as_view(
                        queryset=Blog.objects.all().order_by("-date"),
                        template_name="blog.html")),

	 url(r'^about/$', ListView.as_view(
                        queryset=Blog.objects.all().order_by("-date"),
                        template_name="about.html")),

	 url(r'^contact/$', ListView.as_view(
                       	queryset=Blog.objects.all().order_by("-date"),
                        template_name="contact.html")),

	url(r'^(?P<pk>\d+)$', DetailView.as_view(
		model = Blog,
		template_name="post.html")),

	url(r'^base$', ListView.as_view(
		queryset=Blog.objects.all().order_by("-date"),
		template_name="base.html")),

	)