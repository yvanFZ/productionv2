from django.urls import path
from .views import  LoadUsersPermissions,RegisterUserView,GetCRSFToken, LoginView,LogoutView, CheckAuthenticatedView, DeleteAccountView, HomeView, LockscreenView, UnlockscreenView

app_name = 'authentication'

urlpatterns = [
    path('authenticated', CheckAuthenticatedView.as_view(),name='checkauth'),
    path('loadpermissions', LoadUsersPermissions.as_view()),
    path('delete',DeleteAccountView.as_view()),
    path('login',LoginView.as_view(),name='login'),
    path('register',RegisterUserView.as_view()),
    path('logout',LogoutView.as_view()),
    path('screenlock',LockscreenView.as_view()),
    path('screenunlock',UnlockscreenView.as_view()),
    path('crsf_cookie', GetCRSFToken.as_view(),name='getcookies'),
    path('home', HomeView.as_view()),
]
