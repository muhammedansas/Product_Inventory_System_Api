from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from authentication.models import User


class RegisterViewTest(APITestCase):
    def setUp(self):
        self.url = reverse('regiser')  
        
    def test_register_user(self):
        data = {
            'email': 'test@gmail.com',
            'first_name':'test',
            'last_name':'test',
            'username': 'testuser',
            'password': 'TestPassword123!',
            'confirm_password': 'TestPassword123!'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertIn('email', response.data)
        self.assertEqual(response.data['email'], 'test@gmail.com')
        self.assertTrue(User.objects.filter(email='test@gmail.com').exists())