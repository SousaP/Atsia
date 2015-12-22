from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.utils.translation import gettext as _
from django.shortcuts import render_to_response, render
from proj.models import Blog, Circulos, Emails, Topico, CirculoForum, Participante, Musica, Comentario, Mensagem
from proj.forms import EmailForm, TopicoForm, UserForm, NovoComentario, NovaMensagem
from django.db.models import Q
from django.db import connection, transaction
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Permission
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.db.models import Count
from django.contrib.auth.models import User
from itertools import cycle
from django.http import JsonResponse, HttpResponse
from django.core import serializers
import os
import math
import itertools
# Create your views here.

#vista de um post



def post_view(request, post_id):
	blog = get_object_or_404(Blog, id=post_id)
	return render(request, 'post.html', {'blog': blog})


def nr_paginas_post(request):
	nr_post = Blog.objects.all().count();
	return math.ceil(nr_post/5);


def blog_view_paginas(request,page_id):
	inicio = int(page_id) * 1
	posts = Blog.objects.all().order_by("-date")[inicio:inicio+5]
	hasNext = False
	hasPrevious = False
	if int(page_id) > 0:
		hasPrevious = True
	if nr_paginas_post(request) > int(page_id)+1:
		hasNext = True
	nextPage = int(page_id) +1
	previousPage = int(page_id) -1
	return render(request, 'blog.html', {'object_list': posts, 'hasNext':hasNext, 'hasPrevious': hasPrevious, 'nextPage':nextPage, 'previousPage':previousPage})


def blog_view(request):
	return blog_view_paginas(request,0);

#enviar um email	
@csrf_protect
def post_email(request):
	form = EmailForm(request.POST)
	if form.is_valid():
		form.save()
		return render(request,'contact.html', {})


def nr_paginas_forum(request,forum_id):
	nr_post = Topico.objects.filter(Forum=forum_id,Autorizado=True).count();
	return math.ceil(nr_post/10);



#vista de uma pagina de Forum
def forum_view(request, forum_id):
	return forum_view_pagina(request, forum_id,0);


def forum_view_pagina(request, forum_id,pagina_id):
    if request.user.is_authenticated():
        participante = Participante.objects.get(user=request.user)
        circulo = CirculoForum.objects.get(nome=participante.circulo)
        circuloForum = CirculoForum.objects.get(id=forum_id)
        if (circuloForum.id == circulo.id) | circuloForum.geral:
        	inicio = int(pagina_id) * 10
        	topicos = Topico.objects.filter(Forum=forum_id,Autorizado=True).order_by("-Data")[inicio:inicio+10]
        	#return  render(request,'teste.html', {"erro":topicos})
        	messages = Comentario.objects.filter(TopicoId__in=topicos).values('TopicoId').annotate(Count('TopicoId'))
        	zip_list = list(itertools.zip_longest(topicos, messages))
        	nr_mensagens = verifica_mensagens(request)
        	nr_paginas = nr_paginas_forum(request,forum_id)
        	hasNext = False
        	hasPrevious = False
        	if int(pagina_id) > 0:
        		hasPrevious = True
        	if nr_paginas_forum(request,forum_id) > int(pagina_id)+1:
        		hasNext = True
        	nextPage = int(pagina_id) +1
        	previousPage = int(pagina_id) -1
        	return render(request, 'forum_individual.html', {'lista':zip_list, 'CirculoForum': circuloForum, 'messages':messages, "nr_mensagens":nr_mensagens, 'nr_paginas':range(nr_paginas),'hasNext':hasNext, 'hasPrevious': hasPrevious, 'nextPage':nextPage, 'previousPage':previousPage})
        else:
        	return  HttpResponseRedirect('/login/')
    else:
    	return  HttpResponseRedirect('/login/')



#recebe post criacao post
def post_topico(request, forum_id):
	erro = "comecou"
	if request.user.is_authenticated():
		participante = Participante.objects.get(user=request.user.id)
		circulo = CirculoForum.objects.get(nome=participante.circulo)
		circuloForum = CirculoForum.objects.get(id=forum_id)
		if circuloForum.id == circulo.id:
			#se ta tudo ta tudo			
			form = TopicoForm(request.POST, request.FILES)
			if form.is_valid():
				commit = form.save(commit=False)
				commit.Autor = request.user
				commit.Forum = circuloForum
				commit.Autorizado = False
				if request.FILES.get('Img') != None:
					commit.Img = request.FILES['Img'] # this is my file
					fileName, extension = os.path.splitext(commit.Img.name)
					commit.Img.name = str(commit.id) + str(extension)
				commit.save()
				return HttpResponseRedirect('/forum/')
			else:
				return  render(request,'teste.html', {"erro":erro})
		else:
			return  render(request,'teste.html', {"erro":erro})
	else:
		return  render(request,'teste.html', {"erro":erro})

#vista de uma pagina de criacao de post
def create_post(request, forum_id):
	if request.user.is_authenticated():
		participante = Participante.objects.get(user=request.user.id)
		circulo = CirculoForum.objects.get(nome=participante.circulo)
		circuloForum = CirculoForum.objects.get(id=forum_id)
		if circuloForum.id == circulo.id:
			topicos = Topico.objects.filter(Forum=forum_id)
			return render(request, 'criarTopico.html', {'forum_id':forum_id})
		else:
			return  HttpResponseRedirect('/login/')

	else:
		return  HttpResponseRedirect('/login/')


#vista da pagina principal de Foruns
def forum_principal_view(request):
	return render(request, 'forum.html')


#log-in	
@csrf_protect
def login_view(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			return  HttpResponseRedirect('/forum/')
		else: 
			return render(request,'login.html', {"erro" : "erro login"})
	else:
		return render(request,'login.html', {"erro" : "erro login"})		


#forum - circulos	
def forum_page(request):
    if request.user.is_authenticated():
        participante = Participante.objects.get(user=request.user.id)
        circulo = CirculoForum.objects.filter(nome=participante.circulo)
        geral = CirculoForum.objects.filter(geral=True)
        topicos = Topico.objects.filter(Forum__in=circulo|geral).values('Forum').annotate(Count('Forum'))
        nr_mensagens = verifica_mensagens(request)
        circulos = circulo|geral
        circulos_zip = list(itertools.zip_longest(circulos, topicos))
        return render(request,'forum.html', {"object_list" : circulos_zip, "topicos":topicos, "nr_mensagens" : nr_mensagens})
    else:
        return  HttpResponseRedirect('/login/')


#editar area pessoal	
def edit_names(request):
    if request.method == "POST":
        form = UserForm(request.POST,request.FILES,instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            if request.POST.get("password") == request.POST.get("confirmpassword") and request.POST.get("password") != None and request.POST.get("password") != "":
            	request.user.set_password(request.POST.get("password"))
            	request.user.save()
            user.save()
            if request.FILES.get('Img') != None:
            	participante = Participante.objects.get(user=request.user)
            	participante.Img = request.FILES['Img']
            	fileName, extension = os.path.splitext(participante.Img.name)
            	participante.Img.name = str(request.user.username) + str(extension)
            	participante.save()
            return HttpResponseRedirect('/forum/')
    else:
        form = UserForm(instance=request.user)
        return render_to_response('login.html', locals(),context_instance=RequestContext(request))


#vista de uma pagina de um Topico
def topico_view(request, topico_id):
    comentarios = Comentario.objects.filter(TopicoId=topico_id).order_by("data")
    topico = Topico.objects.get(id=topico_id)
    nr_mensagens = verifica_mensagens(request)
    forum = CirculoForum.objects.get(nome=topico.Forum) 
    respostas = len(comentarios)
    #utilizadores = Comentario.objects.filter(TopicoId=topico_id).order_by("data").values('autor')
    images = []
    for comentario in comentarios:
        image = Participante.objects.filter(user=comentario.autor).values('Img')
        images.append(image)
    #teste = Participante.objects.all()
    #participantes = teste.filter(user__in=comentarios.values('autor')).values('Img')
    participantes_fotos = zip(cycle(comentarios), images)
    return render(request, 'topico.html', {'comentarios_fotos': participantes_fotos, 'comentarios':comentarios, 'topico': topico, "nr_mensagens" : nr_mensagens, 'respostas': respostas, 'forum': forum})

#novo comentario topico	
@csrf_protect
def post_comentario(request, topico_id, outro_comentario):
	form = NovoComentario(request.POST)
	topico = Topico.objects.get(id=topico_id)
	if form.is_valid():
		commit = form.save(commit=False)
		commit.TopicoId = topico
		commit.autor = request.user
		commit.save()
		comentarios = Comentario.objects.filter(TopicoId=topico_id).order_by("data")
		topico = Topico.objects.get(id=topico_id)
		return HttpResponseRedirect('/forum/topico/' + topico_id + '/')
	else:
		comentarios = Comentario.objects.filter(TopicoId=topico_id).order_by("data")
		topico = Topico.objects.get(id=topico_id)
		return HttpResponseRedirect('/forum/topico/' + topico_id + '/')


#forum - circulos	
def pessoal_circulo(request):
	if request.user.is_authenticated():
		participante = Participante.objects.get(user=request.user.id)
		pessoal = Participante.objects.values('user')
		pessoas = User.objects.values('username','id').filter(id__in=pessoal)
		#return render(request,'teste.html', {"erro" : pessoas})
		return render(request,'novamensagem.html', {"pessoas" : pessoas})
	else:
		return  HttpResponseRedirect('/forum/')


#logout
def logout_view(request):
    logout(request)
    return  HttpResponseRedirect('/')


#mensagens
def mensagens_view(request):
	messages_received_False = Mensagem.objects.filter( Q(Destinatario=request.user),Vista=False).values('Autor','Vista','Destinatario').distinct()
	messages_received_True = Mensagem.objects.filter( Q(Destinatario=request.user),Vista=True).values('Autor','Vista').distinct()
	users_received_True = User.objects.filter(Q(id__in=messages_received_True.values('Autor'))).exclude(id__in=messages_received_False.values('Autor')).values('username','id')
	users_received_False = User.objects.filter(id__in=messages_received_False.values('Autor')).values('username','id')
	messages_sent = Mensagem.objects.filter( Q(Autor=request.user)).exclude(Q(Autor__in=messages_received_True.values('Destinatario')) | Q(Autor__in=messages_received_False.values('Destinatario'))).values('Destinatario','Vista').distinct()
	users_sent = User.objects.filter(id__in=messages_sent.values('Destinatario')).values('username','id')
	#return render(request,'teste.html', {'erro':users_received_True})
	return render(request,'mensagens.html', {'messages':users_received_True | users_sent, 'messases_not_read' : users_received_False})


#mensagem
def single_mensage(request,user_id):
    pessoa = User.objects.get(id=user_id)
    message = Mensagem.objects.filter(Q(Autor=user_id,Destinatario=request.user.id) | Q(Destinatario=user_id,Autor=request.user.id)).values('Autor','Texto','data','Destinatario').order_by('data')
    images = []
    for me in message:
        image = Participante.objects.filter(user=me.get('Autor')).values('Img')
        images.append(image)
    messages_zip = zip(cycle(message),images)
    Mensagem.objects.filter(Autor=user_id,Destinatario=request.user.id).update(Vista=True)
    #return render(request,'teste.html', {'erro':pessoa})
    return render(request,'mensagem.html', {'messages_zip':messages_zip, 'pessoa':pessoa})


#post mensagem
@csrf_protect
def post_mensagem(request,user_id):
	form = NovaMensagem(request.POST)
	if form.is_valid():
		commit = form.save(commit=False)
		commit.Autor = request.user
		commit.Destinatario = User.objects.get(id=user_id)
		commit.Vista = False
		commit.save()
		return HttpResponseRedirect('/forum/mensagem/' + user_id + '/')
	else:
		return HttpResponseRedirect('/forum/mensagem/' + user_id + '/')
	


#post mensagem
@csrf_protect
def post_mensagem_inicial(request):
	user_id = request.POST.get('Destinatario')
	#return render(request,'teste.html', {'erro':request.POST})
	return post_mensagem(request,user_id)


def verifica_mensagens(request):
	nr_mensagens = Mensagem.objects.filter(Destinatario = request.user,Vista=False)
	nr_mensagens = len(nr_mensagens)
	return nr_mensagens


def area_pessoal(request):
	img = Participante.objects.get(user=request.user)
	return render(request,'areapessoal.html', {'user':request.user, 'Img':img.Img})


@csrf_protect
def post_removeCom(request):
	commentid = request.POST.get('commentid')
	com = Comentario.objects.get(id=commentid)
	if com.autor == request.user:
		com.delete()
	return HttpResponseRedirect('/forum/topico/' + str(com.TopicoId.id) + '/')



def api_user(request):
	if request.method == "GET":
		password = request.GET.get('passwordL')
		username = request.GET.get('usernameL')
		user = authenticate(username=username, password=password)
		response_data = {}
		if user is not None:
			if user.is_active:
				return JsonResponse({'result':'sucess'})
			else:
				return JsonResponse({'result':'fail'})
		else:
			return JsonResponse({'result':'fail'})


def api_forum(request):
	if request.method == "GET":
		name= request.GET.get('nome')
		user = User.objects.get(username=name)
		participante = Participante.objects.get(user=user.id)
		circulo = CirculoForum.objects.filter(nome=participante.circulo).values("nome")
		geral = CirculoForum.objects.filter(geral=True).values("nome")
		#data = serializers.serialize('json', circulo|geral)
		return HttpResponse(circulo|geral, content_type='application/json')


def api_circulo(request):
	if request.method == "GET":
		forum_id = request.GET.get('forum_id')
		topicos = Topico.objects.filter(Forum=forum_id,Autorizado=True)
		data = serializers.serialize('json', topicos)
		return HttpResponse(data, content_type='application/json')


def api_mensagem(request):
	if request.method == "POST":
		autor = request.POST.get('Autor')
		dest = request.POST.get('Destinatario')
		text = request.POST.get('Texto')
		autor = User.objects.get(username = autor)
		dest = User.objects.get(username = dest)
		novamensagem = Mensagem.objects.create(Autor=autor, Destinatario=dest,Texto=text,Vista = False)
		return JsonResponse({'result':'ok'})

def api_comentario(request):
	if request.method == "POST":
		autor = request.POST.get('Autor')
		idtopico = request.POST.get('idTopico')
		text = request.POST.get('Texto')
		autor = User.objects.get(username = autor)
		topico = Topico.objects.get(id = idtopico)
		NovoComentario = Comentario.objects.create(autor=autor, comentario=text,TopicoId=idtopico)
		return JsonResponse({'result':'ok'})

def api_mensagens(request):
	if request.method == "GET":
		autor = request.POST.get('username')
		otherUser = request.POST.get('otherUser')
		idtopico = request.POST.get('idTopico')
		pessoa = User.objects.get(id=user_id)
		message = Mensagem.objects.filter(Q(Autor=user_id,Destinatario=request.user.id) | Q(Destinatario=user_id,Autor=request.user.id)).values('Autor','Texto','data','Destinatario').order_by('data')
		Mensagem.objects.filter(Autor=user_id,Destinatario=request.user.id).update(Vista=True)
		data = serializers.serialize('json', message)
		return HttpResponse(data, content_type='application/json')
