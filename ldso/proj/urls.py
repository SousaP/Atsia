from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from proj.models import Blog, Circulos, CirculoForum



urlpatterns = patterns('', 
	url(r'^$', ListView.as_view(
		queryset=Blog.objects.all().order_by("-date")[:0],
		template_name="base.html")),

	url(r'^blog/$', ListView.as_view(
                        queryset=Blog.objects.all().order_by("-date")[:10],
                        template_name="blog.html")),

	url(r'^blog/(?P<post_id>[0-9]+)/$', 'proj.views.post_view', name= 'post_view'),

	url(r'^login/$', ListView.as_view(
						model = Blog,
						template_name="login.html")),


	url(r'^forum/$', 'proj.views.forum_page', name= 'forum_page'),

	url(r'^forum/(?P<forum_id>[0-9]+)/$', 'proj.views.forum_view', name= 'forum_view'),

	
	url(r'^about/$', ListView.as_view(
                        queryset=Blog.objects.all().order_by("-date"),
                        template_name="about.html")),

	url(r'^contact/$', ListView.as_view(
                       	queryset=Blog.objects.all().order_by("-date"),
                        template_name="contact.html")),

	url(r'^post_email/$', 'proj.views.post_email', name= 'post_email'),

	url(r'^post_login/$', 'proj.views.login_view', name= 'login_view'),

	url(r'^oquefazemos/$', ListView.as_view(
                        queryset=Blog.objects.all().order_by("-date"),
                        template_name="oquefazemos.html")),

	url(r'^parceiros/$', ListView.as_view(
                        queryset=Blog.objects.all().order_by("-date"),
                        template_name="patrocinios.html")),
	 
	 url(r'^circulos/$', ListView.as_view(
                        queryset=Circulos.objects.all().order_by("-date"),
                        template_name="circulos.html")),

	 url(r'^radio/$', ListView.as_view(
                        model = Blog,
                        template_name="radio.html")),

	url(r'^(?P<pk>\d+)$', DetailView.as_view(
		model = Blog,
		template_name="post.html")),

	url(r'^base$', ListView.as_view(
		queryset=Blog.objects.all().order_by("-date"),
		template_name="base.html")),

	)