from rest_framework.views import APIView
from rest_framework import permissions
from django.utils import timezone , dateformat
from django.core import serializers
from django.contrib.auth import login, logout
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from .serializers import UserSerializer
from rest_framework.response import Response
from users.models import CustomUser,Role,MedewerkerProfile
from users.serializers import MedewerkerSerializer
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator
from django.contrib.auth.hashers import make_password, check_password
from django.middleware.csrf import get_token


class HomeView(APIView):
    def get(self,request, format=None):
        try:
            return Response({'success': 'this is home page'})
        except:
            return Response({'error': 'something went wrong'})

class CheckAuthenticatedView(APIView):
    def get(self,request, format=None):
        user = self.request.user
    
        try:
            isAuthenticated = user.is_authenticated

            if isAuthenticated:
                return Response({ 'isAuthenticated': 'success' })
            else:
                return Response({ 'isAuthenticated':'error'})
        except:
            return Response({'error':'Something when wrong during verify authentication'})


# @method_decorator(csrf_protect, name='dispatch')
class RegisterUserView(APIView):
    # permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        data = self.request.data
        email = data['email']
        is_staff = 0,
        if data['is_staff'] != 'false':
            is_staff = 1
        else:
            is_staff = 0
        password = data['password']
        re_password = data['re_password']
        try:
            if password == re_password:
                if CustomUser.objects.filter(email = email).exists():
                    return Response({ 'error': 'Email already exist'})
                else:
                    if len(password) < 8:
                        return Response({'error': 'Password lengh must be at least 6'})
                    else:
                       
                            user = CustomUser.objects.create(email = email, password = make_password(password),is_staff=is_staff)
                            user.save()
                            return Response({'success':'User successfully created'})
                       
            else:
                return Response({ 'error': 'Passwords do not march'})

        except Exception as e:
                return Response({'error': str(e)})

def authenticate_user(email, password):
    try:
        user = CustomUser.objects.get(email=email)
    except CustomUser.DoesNotExist:
        return None
    else:
        if user.check_password(password):
            return user
        else:
            return None



@method_decorator(csrf_protect, name='dispatch') 
class LoginView(APIView,ModelBackend):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):

        data  = self.request.data
        email = data['email']
        password = data['password']
        user = authenticate_user(email,password)

        if user is not None: 
            login(request,user)
            if user.is_loggedin != True:
                
                user.is_loggedin = True
                user.last_login = dateformat.format(timezone.now(), 'Y-m-d H:i:s')
                user.save()
                return Response({'success':'user is loggedin','email':user.email,})
            else:
                return Response({'success':'user is already loggedin'})                    
        else:
            return Response({'error':'email or passowrd not correct'})
            
            

class LogoutView(APIView):

    def post(self, request, format=None):
        try:
            user = self.request.user
            user.is_loggedin = False
            user.save()
            
            auth.logout(request)

            return Response({'success': 'Loggout successfully','email':user.email})
        except:
            return Response({'error': 'something went wrong when logging out'})

class LockscreenView(APIView):
    def post(self,request,format=None):
        try:
            
            user = self.request.user
            CustomUser.objects.filter(id=user.id).update(is_loggedin=False)
            return Response({'success': 'Screen is locked'})
        except:
            return Response({'error': 'something went wrong when logging out'})
        
class UnlockscreenView(APIView):
    def post(self,request,format=None):
        
        try:
            
            data = self.request.data
            email = data['email']
            password = data['password']
            authUser = authenticate_user(email,password)
            if authUser is not None:
                
                user_ = CustomUser.objects.filter(id=authUser.id).update(is_loggedin=True)
                print(user_)
                user_.save()
                return Response({'success': 'Screen is unlocked'})
            else:
                return Response({'error': 'Wachtwoord niet correct'})
        except:
            return Response({'error': 'something went wrong when logging out'})
        
@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCRSFToken(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        return Response({"message": "Set CSRF cookie"})

# Get all users
class DeleteAccountView(APIView):
    def delete(self, request, format=None):
        user = self.request.user

        try:
            user = CustomUser.objects.filter(id=user.id).delete()
            return Response({'success':'User deleted successfully'})
        except:
            return Response({'error':'Something went wrong when trying to delete user'})



