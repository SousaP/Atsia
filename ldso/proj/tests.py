from django.test import TestCase
from proj.models import Comentario, Topico

class TestBasic2(TestCase):
    "Show setup and teardown"

    def setUp(self):
        self.a = 1
        Comentario.objects.create(TopicoId="2", comentario="Teste comment", autor="1")

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

    #setUp(self):
     #   Comentario.objects.create(TopicoId="2", comentario="Teste comment", autor="1")
        #Comentario.objects.create(TopicoId="1", comentario="Teste comment 2.0", autor="3")

    def test_comentarios(self):
        """Comentarios corretos identified"""
        topico = Topico.objects.get(TopicoId="1")
        test1 = Comentario.objects.get(topico.TopicoId)
        self.assertEqual(test1.comentario, 'Teste comment"')
