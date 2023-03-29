from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MedewerkerSerializer, RoleSerializer, UsersSerializer, FunctieSerializer
from .models import Role,CustomUser, Functie, MedewerkerProfile
from django.contrib.auth.hashers import make_password
from django.db.models import Count
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator
from rest_framework import permissions
# Create your views here.

# KLANTEN AANMAKEN
class PostKlantenView(APIView):
    def post(self, request, format=None):
        if(self.request.data):
            data = self.request.data
           
# MEDEWERKER UPDATED
class UpdateMedewerkersView(APIView):
    def post(self, request, format=None):
        if(self.request.data):
            data = self.request.data
            userObject = {
                'is_active': data['status'],
                'functie_id': data['functie'],
                'email': data['email'],
            }
           
            medewerkerObject = {
                'voornaam': data['voornaam'],
                'tussenvoegsel': data['tussenvoegsel'],
                'achternaam': data['achternaam'],
                'geslacht': data['geslacht'],
                'phone_no': data['phone_no'],
            }
            
            try:
                          
                if CustomUser.objects.filter(email=userObject['email']).update(**userObject):
                    user = CustomUser.objects.filter(email=userObject['email']).values('id')[0]
                    print(user['id'])
                    medewerker = MedewerkerProfile.objects.filter(user_id=user['id']).update(**medewerkerObject)
                    if medewerker:
                        return Response({'success': 'medewerker is met success bijgewerkt'})
                    else:
                        return Response({'error': 'medewerker profile bewerken is niet gelukt'})
                else:
                    return Response({'error': 'user profile bewerken is niet gelukt'})
                
            except Exception as e:
                print(e)
                return Response({'error': str(e)})
            
            
          

# MEDEWERKERS AANMAKEN
@method_decorator(csrf_protect, name='dispatch')
class PostMedewerkersView(APIView):
    permission_classes = (permissions.AllowAny,)
    def createMedewerkerFuncion(self,data):
        medewerker = MedewerkerProfile.objects.create(**data)
        medewerker.save()
        return medewerker
    def post(self, request, format=None):
        if(self.request.data):
            
            data = self.request.data
            # print(type(data))
            re_password = data['re_password']
            userObject ={
                'email':data['email'],
                'is_active' : data['is_active'],
                'functie_id' : data['functie'],
                'password' : data['password'],
                'is_staff': 1,
                'is_loggedin': 0,
            }
            try:
                if CustomUser.objects.filter(email=userObject['email']).exists(): 
                    return Response({'success': 'Medewerker bestaat al'})
                else:
                    if userObject['password'] == re_password:
                       if len(userObject['password']) < 8:
                            return Response({'error': 'wachtwoord moet minimaal 8 charachters '})
                       else:
                            userObject['password'] = make_password(userObject['password'])
                            try:
                                print(userObject)
                                user = CustomUser.objects.create(**userObject)
                                
                            except Exception as e:
                                print(e)
                                return Response({'error': str(e)})
                            user.save()
                            objectMedewerker = {
                                'voornaam': data['voornaam'],
                                'voorletter': data['voorletter'],
                                'geboortdatum': data['geboortDatum'],
                                'tussenvoegsel': data['tussenvoegsel'],
                                'achternaam': data['achternaam'],
                                'geslacht': data['geslacht'],
                                'phone_no': data['phone_no'],
                                'user_id': user.id
                            }
                            try:
                           
                                self.createMedewerkerFuncion(objectMedewerker)
                                return Response({'success': True})
                            except Exception as e: 
                                # print(e)
                                return Response({'error':str(e)})
                    else:   
                        return Response({'error': 'Password doesnt match'})
            except Exception as e:
                # print(e)
                return Response({'error':str(e)})
       
# GET ALL MEDEWERKER API
class GetAllMedewerkersView(APIView):

    def getFunctieMedewerker(self,id):
        user = CustomUser.objects.filter(id=id).values('functie_id')
        user_id = user[0]['functie_id']
        functie = Functie.objects.filter(id=int(user_id)).values('functie','rol_id')
        return functie
    def getRoleName(self,id):
        rol = Role.objects.filter(id=id).values('role_name')
        return rol
    def getuser_data(self,id):
        user = CustomUser.objects.filter(id=id).values('email','is_active')
        return user[0]
    def get(self, request, format=None):
        # medewerkers = MedewerkerProfile.objects.all()
        medewerkersArray = []
        
        medewerkers = MedewerkerProfile.objects.values('id','voornaam','achternaam','geslacht','tussenvoegsel','user_id','phone_no')
        for i in medewerkers:
            functieDatas =  self.getFunctieMedewerker(i['user_id'])
            userDatas = self.getuser_data(i['user_id'])
            # print(functieDatas)
            medewerkerobject = {
            'geslacht': i['geslacht'],
            'voornaam':i['voornaam'],
            'tussenvoegsel': i['tussenvoegsel'],
            'achternaam': i['achternaam'],
            'phone_no': i['phone_no'],
            'functie': functieDatas[0]['functie'],
            'rol_name': self.getRoleName(int(functieDatas[0]['rol_id']))[0]['role_name'],
            'email': userDatas['email'],
            'status': userDatas['is_active']
            }
            
            medewerkersArray.append(medewerkerobject)
        return Response({'context': medewerkersArray,'success': True})

# PASSWORD AANPASSEN
class PasswordAanpassen(APIView):

    def post(self, request, format=None):
        if(self.request.data):

            data = self.request.data
            user = self.request.user
            user_obj = CustomUser.objects.get(id=user.id)    
            oldPassword = data['oldPassword']
            newpassword = data['new_Password']
            if user.check_password(oldPassword):
                user_obj.password = make_password(newpassword)
                # CustomUser.objects.get(id=user.id).update(password = newpassword )
                user_obj.save()
                return Response({
                    'success': 'Wachtwoord met successful created',
                    })
            else:
                return Response({'error':'Incorrect password'})
                            
class RoleListView(APIView):

    def returnCOuntMedewerkers(self,role_id):
        try:
            medewerkers = MedewerkerProfile.objects.filter(rol_id = role_id).count()
            return medewerkers
        except MedewerkerProfile.DoesNotExist:
            return None
        
        # return medewerkerResult

    def get(self,request,format=None):
        roleResult = Role.objects.values_list('id','role_name')
        # data = []
        # for role in roleResult:
            # role_id = role.id
            # medewekerCount = self.returnCOuntMedewerkers(role_id)
            # if medewekerCount == None:
            #     medewekerCount = 0
            # role_name = role.role_name
            # context = {
            #     'id': role_id,
            #     'role_name': role_name,
            #     'medewekerCount': medewekerCount
            # }
            # data.append(context)
            
        # role_Result = RoleSerializer(roleResult,many=True)
        return Response({
            'roles': roleResult,
        })

class RoleView(APIView):

    def post(self,request,format=None):
        # if self.request.is_ajax():
        data = self.request.data
        try:
            if Role.objects.filter(role_name = data['role_name']).exists():
                return Response({
                    'success': False,
                    'message': data['role_name'] + ' already exist ',
                    })
            else:
                role = Role.objects.create(**data)
                role.save()
                return Response({
                    'success': True,
                    'message': data['role_name'] + ' is successfuly created ',
                    })
        except Exception as e:

            return Response({
                'is_success': False,
                'message': str(e)})
    
class GetFunctieView(APIView):

    def returnCOuntMedewerkers(self,id):
        try:
            medewerkers = MedewerkerProfile.objects.filter(functie_id = id).count()
            return medewerkers
        except MedewerkerProfile.DoesNotExist:
            return None

    def get(self,request,format=None):
        functieResult = Functie.objects.values_list('id','functie','rol_id')
        # data = []
        # for functie in functieResult:
        #     functie_id = functie.id
        #     medewekerCount = self.returnCOuntMedewerkers(functie_id)
        #     if medewekerCount == None:
        #         medewekerCount = 0
        #     functie_name = functie.functie
        #     context = {
        #         'id': functie_id,
        #         'functie_name': functie_name,
        #         'medewekerCount': medewekerCount
        #     }
        #     data.append(context)

        return Response({
            'functies': functieResult
        })

class CreateFunctieView(APIView):

    def post(self,request,format=None):
        data = self.request.data
        
        try:
            
            if Role.objects.filter(id = data['rol_id']).exists():
                
                if Functie.objects.filter(functie = data['functie']).exists():
                    return Response({'error':'the functie name exist already'})
                else:
                    print(data['functie'])
                    try:
                        Functie.objects.create(**data)
                        print('succed')
                    except Exception as e:
                        print(str(e))

                    # functie = Functie.objects.create(**data)
                    # functie.save()
                    return Response({'success':'Funcite is successfully created'})
            else:
                return Response({'error': 'Create first role object'})
        except:
            return Response({'error': 'something went wrong with creating the role'})

class GetAllUsersView(APIView):
    # permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        users = CustomUser.objects.all()

        users = UsersSerializer(users, many=True)
        return Response(users.data)

#Get userProfle

class GetUserProfileView(APIView):
    def getFunctieName(self,args):
        functie = Functie.objects.filter(id=args).get()
        # functie = FunctieSerializer(functie)
        return functie

    def get(self, request, format=None):
        try:
            user = self.request.user
            email = user.email
            user_profile = CustomUser.objects.filter(id=user.id).get()
            gebruiker = 'Normale Gebruiker'
            if user_profile.is_superuser == False:
                gebruiker = 'Normale User'
            else:
                gebruiker = 'Super User'
            # MEDEWERKER
            medewerker = MedewerkerProfile.objects.get(user_id=user.id)
            medewerker_ = MedewerkerSerializer(medewerker)
            # idRole = medewerker.rol_id
            # idFunctie = medewerker.functie_id
            # role = Role.objects.get(id=idRole)
            # role = RoleSerializer(role)
            
            functie = self.getFunctieName(user.functie_id)
            role = Role.objects.get(id=functie.rol_id)
            
            return Response({
                'medewerker': medewerker_.data,
                'is_loggedin': user_profile.is_loggedin,
                'email': str(email),
                'role':role.role_name,
                'functie': functie.functie,
                'gebruiker': gebruiker
                })

        except:
            return Response({'error': 'Something went wrong'})
        
# update
class UpdateUserProfileView(APIView):
    def put(self, request, format=None,*args,**kwargs):
        user = self.request.user
        email = user.email
        # firstname = user.firstname
        data = self.request.data
        # first_name = data['first_name']

        # user = CustomUser.objects.get(id=user.id).update(first_name = firstname )
        user = UsersSerializer(user)
        user.save()
        return Response({'profile': user.data, 'email': str(email)})
        # return Response({'success': 'Password successfully aangepast'})

# delete