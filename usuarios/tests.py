from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomUserTests(TestCase):
    def test_crear_usuario(self):
        user_model = get_user_model()
        usr = user_model.objects.create_user(
            username='testuser01',
            email = 'testuser01@gmail.com',
            password='contraseña123#'
        )

        self.assertEqual(usr.username, 'testuser01')
        self.assertEqual(usr.email, 'testuser01@gmail.com')
        self.assertTrue(usr.is_active)
        self.assertFalse(usr.is_staff)
        self.assertFalse(usr.is_superuser)


    def test_crear_superusuario(self):
        user_model = get_user_model()
        usr = user_model.objects.create_superuser(
            username='testsuperuser01',
            email = 'testsuperuser01@gmail.com',
            password='contraseña123#'
        )

        self.assertEqual(usr.username, 'testsuperuser01')
        self.assertEqual(usr.email, 'testsuperuser01@gmail.com')
        self.assertTrue(usr.is_active)
        self.assertTrue(usr.is_staff)
        self.assertTrue(usr.is_superuser)






        

            
