from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.test import Client, TestCase
from users.models import CustomUser,Functie,Role

class UserLoginTests(APITestCase):

    # def create_user(self,**args):
        # role = 
    # def __init__(self,**args):
        # self.role_name = args.role_name
    def create_user(self, **args):
        role = {'role_name':args['role_name']}
        role = Role.objects.create(**role)
        func = {'functie':args['functie'],'rol_id':role.id}
        functie = Functie.objects.create(**func)
        user = {
            "email":args['email'],
            # "voornaam": "Yvan",
            # "voorletter": "Y",
            # "tussenvoegsel": "Van",
            # "achternaam": "Mutara",
            # "geslacht": "Dhr",
            # "geboortDatum":"24-05-1988",
            # "phone_no":"+31687621114",
            "functie": functie,
            "is_superuser":1,
            # "permissions": "add_permission",
            "is_active":1,
            "is_staff": 1,
            "password": args['password'],
            #"re_password": "test1234567"
        }
        self.user = CustomUser.objects.create_user(**user)
        return self.user

        
    def login(self,**data):
        # data = {'role_name':'R&D','functie':'Data analist','email':'test@test.nl','password':'testtersfstuu'}
        # self.user = self.logInUser(**data)
        login_data = {'email':'test@test.nl','password':'testtersfstuu'}
        url = reverse('auth:login')
        response = self.client.post(url,login_data)
        self.client.credentials(HTTP_AUTHORIZATION="Bear {response.data}")
        self.client.force_login(self.user)
        url = reverse('mpo:getmpo')
        data = {"id": 1}
        response = self.client.post(url,data)
        self.assertEqual(response.status_code ,status.HTTP_200_OK)
 