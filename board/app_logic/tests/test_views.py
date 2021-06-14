from django.test import TestCase
from django.urls import reverse


class WelcomePageTest(TestCase):
    def test_welcome_page(self):
        url = reverse('welcome')
        responce = self.client.get(url)
        self.assertEqual(responce.status_code, 200)
        self.assertContains(responce, 'Добро пожаловать!')