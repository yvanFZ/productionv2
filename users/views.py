from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MedewerkerSerializer, UsersSerializer
from .models import Role,CustomUser, Functie, MedewerkerProfile
from django.contrib.auth.hashers import make_password
from rest_framework import permissions
from django.contrib.auth.models import Permission
from django.db import transaction
from permissions.medewerkerpermissions import permission_required


from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
# Create your views here.

# KLANTEN AANMAKEN
class PostKlantenView(APIView):
    def post(self, request, format=None):
        if(self.request.data):
            data = self.request.data

class LoadProjectleiders(APIView):
    permission_1 = "view_customuser"
    permission_2 = "add_permission"
    permission_classes = [permission_required(permission_1) | permission_required(permission_2)]
    #get all users met functie projectleider
    def get_all_users_met_functie_projectleider():
        data = CustomUser.objects.filter(functie_id__in = [2]).exists()
        return data
    def get(self,request,format):
        data = MedewerkerProfile.objects.filter(player__name__in = []).exists()
        return Response({'data': data})
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
    # permission_classes = [permission_required("add_customuser") | permission_required("add_permission")]
 
    def add_permissions_to_user(self,permissions,user_id):
        user = CustomUser.objects.get(id=user_id)
        try:

            with transaction.atomic():
                for i in permissions:
                    permission = Permission.objects.get(codename=i)
                    user.user_permissions.add(permission)
                    user.save()
                   
            return True
        except Exception as e:
            return str(e)
        
    def createMedewerkerFuncion(self,data):
        medewerker = MedewerkerProfile.objects.create(**data)
        medewerker.save()
        return medewerker
    
    def post(self, request, format=None):
        if(self.request.data):
            data = self.request.data
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
                            self.add_permissions_to_user(data['permissions'],user.id,)
                            # Check wich pages and permissions the user has
                            # update table users_permissions in database
                            try:
                                self.createMedewerkerFuncion(objectMedewerker)
                                # 
                                return Response({'success': 'Medewerker is successfuly toegevogd'})
                            except Exception as e: 
                            
                                return Response({'error':str(e)})
                    else:   
                        return Response({'error': 'Password doesnt match'})
            except Exception as e:
               
                return Response({'error':str(e)})
       
# GET ALL MEDEWERKER API
class GetAllMedewerkersView(APIView):
    permission_classes = [permission_required("view_customuser") | permission_required("add_permission")]
    def get_queryset(self):
        return  MedewerkerProfile.objects.values('id','voornaam','achternaam','geslacht','tussenvoegsel','user_id','phone_no')
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
     
        medewerkersArray = []
        medewerkers = self.get_queryset()
        for i in medewerkers:
            functieDatas =  self.getFunctieMedewerker(i['user_id'])
            userDatas = self.getuser_data(i['user_id'])
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
                    try:
                        Functie.objects.create(**data)
                        
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

# Get userProfle


class GetALLMedewerkersPermissions(APIView):
    permission_classes = [permission_required("add_permission")]
    def get(self,request,format=None):
        # get all apps from content_type table
        apps = Permission.objects.values('name','codename')
       
        return Response({'data': apps})
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