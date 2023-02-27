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
          

# MEDEWERKERS AANMAKEN
@method_decorator(csrf_protect, name='dispatch')
class PostMedewerkersView(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        if(self.request.data):
            data = self.request.data
            email = data['email']
            voornaam = data['voornaam']
            voorletter = data['voorletter']
            tussenvoegsel = data['tussenvoegsel']
            achternaam = data['achternaam']
            geslacht = data['aanhef']
            functie = data['functie']
            role = data['role']
            phone = data['phone']
            geboortdatum = data['geboortDatum']
            is_actif = data['status']
            password = data['password']
            re_password = data['re_password']
            try:
                if CustomUser.objects.filter(email=email).exists():
                    # Update

                    return Response({'success': True})
                else:
                    
                    if password == re_password:
                        if len(password) < 8:
                            
                            return Response({'error': False})
                        else:
                            is_actif_ = 0
                            if is_actif == "Actif":
                                is_actif_ = 1
                        
                            user = CustomUser.objects.create(email = email,password = make_password(password),is_active=is_actif_,is_staff = 1)
                            user.save()
                            medewerker = MedewerkerProfile.objects.create(
                                voornaam = voornaam,
                                voorletter = voorletter,
                                tussenvoegsel = tussenvoegsel,
                                achternaam = achternaam,
                                geslacht = geslacht,
                                geboortdatum = geboortdatum,
                                phone_no = phone,
                                functie_id = functie,
                                rol_id = role,
                                user_id = user.id
                            )
                            try:
                                medewerker.save()
                                return Response({'success': True})
                            except Exception as e: 
                                return Response({'error':str(e)})
                    else:   
                        return Response({'error': 'Password doesnt match'})  
            
            except Exception as e: 
                return Response({'error':str(e)})
            

            
# GET ALL MEDEWERKER API
class GetAllMedewerkersView(APIView):
    def get(self, request, format=None):

      
        medewerkers = MedewerkerProfile.objects.all()

        ids = []
        aanhefs = []
        voornaams = []
        tussenvoegsels = []
        achternaams = []
        functies = []
        roles = []
        gebruikers = []
        phones = []
        emails = []
        status = []

        # Roles
        roleResult = Role.objects.all()
        role_Result = RoleSerializer(roleResult,many=True)

        # Functies
        functieResult = Functie.objects.all()
        functie_Result = FunctieSerializer(functieResult,many=True)
        # GET Functie Naam
        def getFunctieNaam(functieID):
            functies = Functie.objects.all()
            functie_name = ''
            for functie in functies.iterator():
                if functie.id == functieID:
                    functie_name = functie.functie
            return functie_name
        # GET STATUS
        def getStatusUser(userId):

            users = CustomUser.objects.all()
            status = ''
            for user in users.iterator():
                if user.id == userId:
                    is_active = user.is_active
                    if is_active == 1 :
                        status = 'Actif' 
                    
                    else:
                        status = 'Inactif'
                    
            return status
        # GET Email
        def getEmailUser(userId):

            users = CustomUser.objects.all()
            email = ''
            for user in users.iterator():
                if user.id == userId:
                    email = user.email
                    
            return email
        
        # GET Gebruiker
        def getUsergebruiker(userId):

            users = CustomUser.objects.all()
            gebruiker = ''
            for user in users.iterator():
                if user.id == userId:
                    is_superuser = user.is_superuser
                    if is_superuser == 1:
                        gebruiker = 'Super User'
                    else:
                        gebruiker = 'Normale gebruiker'
                    
            return gebruiker
        
        
        # GET Role Naam
        def getRoleNaam(roleID):
            roles = Role.objects.all()
            role_name = ''
            for role in roles.iterator():
                if role.id == roleID:
                    role_name = role.role_name
            return role_name

        for medewerker in medewerkers.iterator():
            id = medewerker.id
            ids.append(id)
            aanhef = medewerker.geslacht
            aanhefs.append(aanhef)
            voornaam = medewerker.voornaam
            voornaams.append(voornaam)
            tussenvoegsel = medewerker.tussenvoegsel
            tussenvoegsels.append(tussenvoegsel)
            achternaam = medewerker.achternaam
            achternaams.append(achternaam)
            functie = getFunctieNaam(medewerker.functie_id)
            functies.append(functie)
            role = getRoleNaam(medewerker.rol_id)
            roles.append(role)
            gebruiker = getUsergebruiker(medewerker.user_id)
            gebruikers.append(gebruiker)
            phone =  str(medewerker.phone_no)
            phones.append(phone)
            email = getEmailUser(medewerker.user_id)
            emails.append(email)
            is_active = getStatusUser(medewerker.user_id)
            status.append(is_active)
        
        context = [
            {
                'id': i,
                'aanhef': j,
                'voornaam': k,
                'tussenvoegsel': a,
                'achternaam': b,
                'functie': c,
                'role': d,
                'gebruiker': e,
                'phone': f,
                'email': g,
                'status': h
                } for i, j, k, a,b,c,d,e,f,g,h in zip(
                    ids, 
                    aanhefs,
                    voornaams,
                    tussenvoegsels,
                    achternaams,
                    functies,
                    roles,
                    gebruikers,
                    phones,
                    emails,
                    status
      
                    )
                ]

        return Response({
            'success': True,
            'context': context,
            'roles': role_Result.data,
            'functies': functie_Result.data
          
            })


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
        roleResult = Role.objects.all()
        data = []
        for role in roleResult:
            role_id = role.id
            medewekerCount = self.returnCOuntMedewerkers(role_id)
            if medewekerCount == None:
                medewekerCount = 0
            role_name = role.role_name
            context = {
                'id': role_id,
                'role_name': role_name,
                'medewekerCount': medewekerCount
            }
            data.append(context)
            
        # role_Result = RoleSerializer(roleResult,many=True)
        return Response({
            'roles': data
        })

class RoleView(APIView):

    def post(self,request,format=None):
        # if self.request.is_ajax():
        data = self.request.data
        role_name = data['role']
        try:
            if Role.objects.filter(role_name = role_name).exists():
                return Response({
                    'is_success': False,
                    'message': role_name + ' already exist ',
                    })
            else:
                role = Role.objects.create(role_name = role_name)
                role.save()
                return Response({
                    'is_success': True,
                    'message': role_name + ' is successfuly created ',
                    })
        except Exception as e:

            return Response({
                'is_success': False,
                'message': str(e)})
        # else:
        #     if self.request.data:
        #         data = self.request.data
        #         role = Role.objects.create(role_name = role_name)
        #         role.save()



    
class GetFunctieView(APIView):

    def returnCOuntMedewerkers(self,id):
        try:
            medewerkers = MedewerkerProfile.objects.filter(functie_id = id).count()
            return medewerkers
        except MedewerkerProfile.DoesNotExist:
            return None

    def get(self,request,format=None):
        functieResult = Functie.objects.all()
        data = []
        for functie in functieResult:
            functie_id = functie.id
            medewekerCount = self.returnCOuntMedewerkers(functie_id)
            if medewekerCount == None:
                medewekerCount = 0
            functie_name = functie.functie
            context = {
                'id': functie_id,
                'functie_name': functie_name,
                'medewekerCount': medewekerCount
            }
            data.append(context)

        return Response({
            'functies': data
        })

class CreateFunctieView(APIView):

    def post(self,request,format=None):
        data = self.request.data
        functie_name = data['functie']
        rol_id = data['role']
        try:
            if Role.objects.filter(id = rol_id).exists():
                if Functie.objects.filter(functie = functie_name).exists():
                    return Response({'error':'the functie name exist already'})
                else:
                    role = rol_id
                    functie_name = functie_name
                    functie = Functie.objects.create(functie = functie_name,rol_id = role)
                    functie.save()
                    return Response({'success':'Funcite is successfully created'})
            else:
                return Response({'error': 'Create first role object'})
        except:
            return Response({'error': 'something went wrong with creating the role'})

#Read

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
        return functie.functie

    def get(self, request, format=None):
        try:
            user = self.request.user
            email = user.email
            user_profile = CustomUser.objects.get(id=user.id)
            gebruiker = 'Normale Gebruiker'
            if user_profile.is_staff == False:
                gebruiker = 'Normale User'
            else:
                gebruiker = 'Super User'
            # MEDEWERKER
            medewerker = MedewerkerProfile.objects.get(user_id=user.id)
            medewerker_ = MedewerkerSerializer(medewerker)
            idRole = medewerker.rol_id
            idFunctie = medewerker.functie_id
            role = Role.objects.get(id=idRole)
            role = RoleSerializer(role)
            functie = self.getFunctieName(idFunctie)
            
                
            return Response({
                'medewerker': medewerker_.data, 
                'email': str(email),
                'role':role.data,
                'functie': functie,
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