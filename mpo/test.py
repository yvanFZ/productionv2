from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from authentication.test import TestAuthentification
class TestMpoCase(APITestCase):
    data = {'role_name':'R&D','functie':'Data analist','email':'test@test.nl','password':'testtersfstuu'}
    # def setUp(self):
    #     client = self.client
    # data = {'role_name':'R&D','functie':'Data analist','email':'test@test.nl','password':'testtersfstuu'}
    def test_get_mpo(self):
        
        # user = UserLoginTests().login(**self.data)
        # if user :
        #     print(1)
        # else:
        #     print(0)
        
        TestAuthentification().test_login_user(**self.data)
        url = reverse('mpo:getmpo')
        data = {'id':'1'}
        response = self.client.post(url,data)
        print(response)
        self.assertEqual(response.status_code ,status.HTTP_403_FORBIDDEN)
 


