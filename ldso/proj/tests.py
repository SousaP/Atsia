from django.test import TestCase
from datetime import datetime
from django.contrib.auth.models import User
from proj.models import *

class TestBasic2(TestCase):
    "Show setup and teardown"

    def setUp(self):
        self.a = 1
        self.Circle = CirculoForum.objects.create(nome="Braga", descricao="Test Circle")
        self.Utilizador = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        self.Part = Participante.objects.create(user=self.Utilizador, circulo=self.Circle)
        self.Topic = Topico.objects.create(Forum=self.Circle, Titulo="Teste Topic", Descricao="Test Topic Description", Autor=self.Utilizador, Autorizado=False)
        Comentario.objects.create(TopicoId=self.Topic, comentario="Teste comment", autor=self.Utilizador)

    def tearDown(self):
        del self.a

    def test_basic1(self):
        "Basic with setup"

        self.assertNotEqual(self.a, 2)

    def test_basic2(self):
        "Basic2 with setup"
        assert self.a != 2

    def test_fail(self):
        "This test should fail"
        assert self.a == 2

    def test_comentarios(self):
        """Correct commentaries identified"""
        test1 = Comentario.objects.get(TopicoId=self.Topic)
        self.assertEqual(test1.comentario, 'Teste comment')

    def test_default_authorized(self):
        """Check default from topico"""
        self.assertEqual(self.Topic.Autorizado, False)

    def test_default_geral(self):
        """Check default from CirculoForum"""
        self.assertEqual(self.Circle.geral, False)
