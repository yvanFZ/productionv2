from django.urls import path
from .views import  LoadUsersPermissions,RegisterUserView,GetCRSFToken, LoginView,LogoutView, CheckAuthenticatedView, DeleteAccountView, HomeView, LockscreenView, UnlockscreenView

app_name = 'authentification'

urlpatterns = [
    path('authenticated', CheckAuthenticatedView.as_view()),
    path('loadpermissions', LoadUsersPermissions.as_view()),
    path('delete',DeleteAccountView.as_view()),
    path('login',LoginView.as_view()),
    path('register',RegisterUserView.as_view()),
    path('logout',LogoutView.as_view()),
    path('screenlock',LockscreenView.as_view()),
    path('screenunlock',UnlockscreenView.as_view()),
    path('crsf_cookie', GetCRSFToken.as_view()),
    path('home', HomeView.as_view()),
]
