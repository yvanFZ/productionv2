from django.urls import path, re_path
from .views import GetALLMedewerkersPermissions,GetFunctieView,RoleListView,PostMedewerkersView,GetAllMedewerkersView,PasswordAanpassen,RoleView,CreateFunctieView , GetAllUsersView, GetUserProfileView, UpdateUserProfileView,UpdateMedewerkersView
from . import testview 

urlpatterns = [
    path('create-role',RoleView.as_view()),
    path('role',RoleListView.as_view()),
    path('functie',GetFunctieView.as_view()),
    path('create-functie',CreateFunctieView.as_view()),
    # path('create-medewerkerprofile',CreateUserProfileView.as_view()),
    # path('create-klantprofile',CreateUserProfileView.as_view()),
    path('get-Allusers',GetAllUsersView.as_view()),
    path('user-profile',GetUserProfileView.as_view()),
    path('user-resetPassword',PasswordAanpassen.as_view()),
    path('user-update',UpdateUserProfileView.as_view()),
    path('get-allmedewerkers',GetAllMedewerkersView.as_view()), # this route will change in the future
    path('all-medewerkerAanmaken',PostMedewerkersView.as_view()), # this route will change in the future
    path('medewerkers_update',UpdateMedewerkersView.as_view()), 
    path('get-all_medewerkers_permissions',GetALLMedewerkersPermissions.as_view()),
    # test urls 
    re_path('<int:id>',testview.index, name='index'),
    path('',testview.login_user,name="login"),
    re_path(r'^logout/$',testview.logout_user,name='logout'),
    re_path(r'^home/$',testview.home,name="home"),
    #SEARCH MEDEWERKERS ROUTES
     re_path(r'post/ajax/medewerkers/$',testview.seacrhUser_RoleForm, name="user_role_form"),
    # ROLE ROUTES
    re_path(r'^roleoverzicht$',testview.roleOverzicht, name='roleoverzicht'),
    re_path(r'^roleoverzicht/createrole$',testview.create_role, name='createrole'),
    re_path(r'^medewerkeruitrole/(?P<id>\d+)/$',testview.rolemedewerkerverwijderen, name='medewerkeruitrole'),
    re_path(r'^roleoverzichtbewerken/(?P<id>\d+)/$',testview.roleOverzichtbewerken, name='rolebewerken'),
    re_path('get/ajax/medewerkers/',testview.view_role_medewerker, name="add_role_bewerken"),
    re_path(r'post/ajax/medewerkeruitrole/$',testview.rolemedewerkerverwijderen, name="medewerker-role"),
    # FUNCTIE ROUTES
    re_path(r'^functieoverzichtbewerken/(?P<id>\d+)/$',testview.functieOverzichtbewerken, name='functiebewerken'),
    re_path(r'^functiteoverzicht/$',testview.functieoverzicht, name='functieoverzicht'),
    re_path(r'^functiteoverzicht/createfunctie$',testview.create_functie, name='createfunctie'),
    re_path(r'^functieoverzichtbewerken/(?P<id>\d+)/ajax/functie/medewerkers$',testview.view_functie_medewerker, name="add_medewerker_in_functie"),
    re_path(r'^functieoverzichtbewerken/(?P<id>\d+)/ajax/functie/medewerkersdelete',testview.functiemedewerkerverwijderen, name="delete_medewerker_in_functie"),
    # MEDEWERKER ROUTES
    re_path(r'^medewerkeroverzicht/$',testview.medewerkeroverzicht, name='medewerkeroverzicht'),
    re_path(r'^medewerkeroverzicht/createmedewerker$',testview.createmedewerker, name='createmedewerker'),
    re_path(r'^register/$',testview.create_user, name='register'),
    
    # KLANT ROUTES 
    re_path(r'^klantenoverzicht/$',testview.klantoverzicht, name='klantenoverzicht'),
    re_path('createklant/',testview.klantcreate, name='createklant'),
    
    re_path(r'^medewerkerbewerken/(?P<id>\d+)/$',testview.medewerkerbewerken, name='medewerkerbewerken'),
    re_path(r'^createmedewerker/$',testview.createmedewerker, name='createmedewerker'),
    re_path(r'^userprofile/(?P<id>\d+)/$',testview.userprofile, name='userprofile'),

    #NAVBAR ROUTES
    re_path(r'^navbarqueryset$',testview.getNavbarData, name='navbar'),

   
]
