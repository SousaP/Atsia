from django.shortcuts import render, get_object_or_404
from proj.models import Blog, Circulos, Emails, Topico, CirculoForum, Participante, Musica, Comentario
from proj.forms import EmailForm, TopicoForm, UserForm, NovoComentario
from django.utils.translation import gettext as _
from django.shortcuts import render_to_response, render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
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

#vista de uma pagina de Forum
def forum_view(request, forum_id):
	if request.user.is_authenticated():
		participante = Participante.objects.get(user=request.user)
		circulo = CirculoForum.objects.get(nome=participante.circulo)
		circuloForum = CirculoForum.objects.get(id=forum_id)
		if circuloForum.id == circulo.id:
			topicos = Topico.objects.filter(Forum=forum_id)
			return render(request, 'forum_individual.html', {'topicos':topicos, 'CirculoForum': circuloForum})
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
			form = TopicoForm(request.POST)
			if form.is_valid():
				commit = form.save(commit=False)
				commit.Autor = request.user
				commit.Forum = circuloForum
				commit.Autorizado = False
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
		return render(request,'forum.html', {"object_list" : circulo})
	else:
		return  HttpResponseRedirect('/login/')


#editar area pessoal	
def edit_names(request, template_name="editarprofile.html"):
    if request.method == "POST":
        form = UserForm(data=request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return HttpResponseRedirect('/areapessoal/')
    else:
        form = UserForm(instance=request.user)
    return render_to_response(template_name, locals(),
        context_instance=RequestContext(request))


#vista de uma pagina de um Topico
def topico_view(request, topico_id):
	comentarios = Comentario.objects.filter(TopicoId=topico_id).order_by("data")
	topico = Topico.objects.get(id=topico_id)
	return render(request, 'topico.html', {'comentarios':comentarios, 'Topico': topico})


#novo comentario topico	
@csrf_protect
def post_comentario(request, topico_id):
	form = NovoComentario(request.POST)
	topico = Topico.objects.get(id=topico_id)
		 

	if form.is_valid():
		commit = form.save(commit=False)
		commit.TopicoId = topico
		commit.autor = request.user
		commit.save()
		return render(request,'forum.html')
	else:
		return  render(request,'/forum/')

#forum - circulos	
def pessoal_circulo(request):
	if request.user.is_authenticated():
		participante = Participante.objects.get(user=request.user.id)
		pessoal = Participante.objects.filter(circulo=participante.circulo).values('id')
		pessoas = User.objects.values('username').filter(id__in=pessoal)
		return render(request,'novamensagem.html', {"pessoas" : pessoas})
	else:
		return  HttpResponseRedirect('/forum/')