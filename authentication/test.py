from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from users.test import UserLoginTests

class TestAuthentification(APITestCase):

    def test_auth_get_cookies(self):
        url = reverse('authentication:getcookies')
        response = self.client.get(url)
        cookie = response.client.cookies['csrftoken'].value
        print(cookie)
        # self.client.credentials(HTTP_AUTHORIZATION=f"Bear {response.data}")
        # self.assertEqual(response.status_code ,status.HTTP_200_OK)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bear {cookie}")

    def test_login_user(self,**kwargs):
        
        UserLoginTests().create_user(**kwargs)
        url = reverse('authentication:login')
        response = self.client.post(url,email=kwargs['email'],password=kwargs['password'])
        print(response)
        # print(response)
        # self.client.credentials(HTTP_AUTHORIZATION=f"Bear {response.data}")
    