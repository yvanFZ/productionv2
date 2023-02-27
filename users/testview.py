from urllib import request
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.csrf import csrf_exempt
from .serializers import MedewerkerSerializer
from django.shortcuts import get_object_or_404, render, redirect
# from hashids import Hashids
from django.utils import timezone, dateformat
from .models import Role, MedewerkerProfile, CustomUser, Functie
from django.contrib.auth import  login, logout
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.decorators import login_required
import datetime
from django.http import JsonResponse
from django.db.models import Q
from django.core.serializers import serialize
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.views.generic import ListView





# @login_required
@login_required
def seacrhUser_RoleForm(request):
    try:
        if request.is_ajax():
            res = None
            str_ = request.POST.get('str')
            # qs = MedewerkerProfile.objects.filter(Q(voornaam = str_) | Q(achetnaam = str_))
            qs = MedewerkerProfile.objects.filter(Q(achternaam__icontains=str_) | Q(voornaam__icontains=str_) )
            if len(qs) > 0 and len(str_) > 0:
                data = []
                for pos in qs:
                    item = {
                        'pk':pos.pk,
                        'fn': pos.voornaam,
                        'ln': pos.achternaam,
                        'date_ofbirth': str(pos.geboortdatum)

                    }
                    data.append(item)
                res = data
            else:
                res = 'Medewerker niet gevonden ...'
            # serializer = serializers.serialize('json',res)
            return JsonResponse({'data': res})
        else:
            return JsonResponse({"nothing":"posted"})
    except Exception as e:
        messages.success(request,str(e))
        return JsonResponse({"nothing":str(e)})

@login_required
def view_role_medewerker(request):
    #request should be ajax and method should be get.
    try:
        if request.is_ajax():
            # res = None
            idrole = request.POST.get('idrole')
            idmedewerker = request.POST.get('idmedewerker')
            # define the medewerker role id if is not none
            medewerker = MedewerkerProfile.objects.filter(id=idmedewerker).get()
            if medewerker.rol_id == None:
                MedewerkerProfile.objects.filter(id=idmedewerker).update(rol_id=idrole)
                return JsonResponse({
                    'is_success': True,
                    'success': ' is successvol toegevoegd',
                    'medewerker':medewerker.voornaam})
                
            else:
                return JsonResponse({
                    'is_success': False,
                    'error':' kan alleen een role hebben',
                    'medewerker': medewerker.voornaam})
                
    except Exception as e:
        messages.success(request,str(e))
        return JsonResponse({"nothing":str(e)})







@login_required
def index(response, id):
    user = MedewerkerProfile.objects.get(id=id)
    return render(response, 'base.html',{
        'user': user
    })


#role overzicht
@login_required
def roleOverzicht(request):
    counts = []
    role_namen = []
    role_ids = []
    roles = Role.objects.all()
    for role in roles:
        if role.role_name != None:
            count = MedewerkerProfile.objects.filter(rol_id = role.id).count()
            counts.append(count)
            role_name = role.role_name
            role_id = role.id
            role_ids.append(role_id)
            role_namen.append(role_name)
        else:
            return JsonResponse({
                'is_success': False,
                'message': 'cant find the array'
            })
    
    context = zip(role_ids,role_namen,counts)

    if request.is_ajax():
        if request.method == 'GET':
            serialized_q = json.dumps(list(context), cls=DjangoJSONEncoder)
            return JsonResponse({
                'data': serialized_q
            #    'ids': role_id,
            #    'names': role_name,
            #    'counts': count
            })
    else:

        return render(request,'role/roleoverzicht.html',{
        'context':context,})
    
    # print(context)
    


#role medewerker delete
@login_required
def rolemedewerkerverwijderen(request):
    if request.is_ajax():
        user_id = request.POST.get('idmedewerker')
        # role_id = request.POST.get('idrole')
        medewerker = MedewerkerProfile.objects.filter(id=user_id).get()
        MedewerkerProfile.objects.filter(id=user_id).update(rol_id=None,functie_id=None)
        return JsonResponse({
            'success': ' is successfuly uit de role table verwijderd',
            'medewerker': medewerker.voornaam})    
    else:
        return JsonResponse({'error':'something went wrong'})
    # messages.success(request,'Gebruiker is uit role gehaald')
    # return redirect('rolebewerken ')



# role update
@login_required
def roleOverzichtbewerken(request,id):
        role = Role.objects.filter(id=id).get()
        role_name = role.role_name
        role_id = role.id
        medewerkers = MedewerkerProfile.objects.filter(rol_id =id)
        return render(request,'role/roleoverzichtbewerken.html',{
            'medewerkers':medewerkers,
            'role_id':role_id,
            'role_name': role_name
        })
# create role




@login_required
def create_role(request):
    if request.is_ajax():
        if request.method == 'POST':
            role_name = request.POST['str']
            created_at =  datetime.datetime.now()
        
            try:
                if Role.objects.filter(role_name=role_name).exists():
                    return JsonResponse({
                        'is_success': False,
                        'message': role_name + ' bestaat al',})
                else:
                    role = Role.objects.create(role_name=role_name,created_at = created_at)
                    role.save()
                    # messages.success(request,'role created successfully')
                    return JsonResponse({
                        'is_success': True,
                        'message': role_name + ' bcreated successfully',})
                
            except Exception as e:
                # messages.success(request,str(e))
                return JsonResponse({
                    'is_success': True,
                    'message': role_name + ' bcreated successfully',})
        else:
            return JsonResponse({
                    'is_success': True,
                    'message': role_name + ' bcreated successfully',})
    else:
        return JsonResponse({
                'is_success': True,
                'message': role_name + ' bcreated successfully',})


#functie overzicht

@login_required
def functieoverzicht(request):
    counts = []
    functie_namen = []
    functie_ids = []
    functies = Functie.objects.all()
    for functie in functies:
        if functie.functie != None:
            count = MedewerkerProfile.objects.filter(functie_id = functie.id).count()
            counts.append(count)
            functie_name = functie.functie
            functie_id = functie.id
            functie_ids.append(functie_id)
            functie_namen.append(functie_name)
        else:
            return JsonResponse({
                'is_success': False,
                'message': 'cant find the array'
            })
    
    context = zip(functie_ids,functie_namen,counts)
    
    # print(type(context))
    if request.is_ajax():
        if request.method == 'GET':
            serialized_q = json.dumps(list(context), cls=DjangoJSONEncoder)
            return JsonResponse({
                'data': serialized_q
            #    'ids': role_id,
            #    'names': role_name,
            #    'counts': count
            })
        elif request.method == 'POST':
            roleID = request.POST['id']
            qs = Functie.objects.filter(rol_id = roleID)
            qs_serialize= json.loads(serialize('json', qs))
            return JsonResponse({
                'response': qs_serialize
            #    'ids': role_id,
            #    'names': role_name,
            #    'counts': count
            })
        else:

            return JsonResponse({
                'id': roleID
            #    'ids': role_id,
            #    'names': role_name,
            #    'counts': count
            })
    else:
        roles = Role.objects.all()
        return render(request,'functie/functieoverzicht.html',{
        'context':context,
        'roles':roles})

# create functie 
@login_required
def create_functie(request):

    if request.method == 'POST':
        functie = request.POST['functie']
        roleid= request.POST['role']
        # created_at =  datetime.datetime.now()
        if request.is_ajax():
            try:
                queryset = Functie.objects.get(functie=functie,rol_id=roleid)
                    
                return JsonResponse({
                    'is_success': False,
                    'success': queryset,
                    })
                
            except Exception as e:
                    if Functie.objects.filter(functie = functie).exists():
                        if Functie.objects.filter(rol_id = roleid).exists():

                            return JsonResponse({
                            'is_success': False,
                            'success': functie + ' bestaal al',
                            })
                        else:
                            role_id = roleid
                            functie = Functie.objects.create(functie = functie,rol_id = role_id)
                            
                            return JsonResponse({
                                'is_success': True,
                                'success': str(functie) + ' is successfuly created',
                                })
                       
                    else:
                        role_id = roleid
                        functie = Functie.objects.create(functie = functie,rol_id = role_id)

                        return JsonResponse({
                            'is_success': True,
                            'success': str(functie) + ' is successfuly created',
                            })
                # return JsonResponse({
                #             'is_success': False,
                #             'success': str(e),
                #             })

        else:
            roles = Functie.objects.all()
            return render(request, 'functie/functieoverzicht.html',{
                'roles': roles
            })
@login_required
def functieOverzichtbewerken(request,id):
    functie = Functie.objects.filter(id=id).get()
    functie_name = functie.functie
    functie_id = functie.id
    medewerkers = MedewerkerProfile.objects.filter(functie_id =id)
    return render(request, 'functie/functieoverzichtbewerken.html',{
        'medewerkers': medewerkers,
        'functie_id':functie_id,
        'functie_name': functie_name
        })

@login_required
def view_functie_medewerker(request,id):
    #request should be ajax and method should be get.
    try:
        if request.is_ajax():
            # res = None
            idfunctie = request.POST.get('idfunctie')
            idmedewerker = request.POST.get('idmedewerker')
            # define the medewerker functie id if is not none
            medewerker = MedewerkerProfile.objects.filter(id=idmedewerker).get()
            functie = Functie.objects.filter(id=idfunctie).get()
            role = functie.rol_id

            if medewerker.rol_id == None and medewerker.functie_id == None:
                MedewerkerProfile.objects.filter(id=idmedewerker).update(functie_id=idfunctie,rol_id=role)
                return JsonResponse({
                    'is_success': True,
                    'message': str(medewerker) + ' is successvol toegevoegd',
                    })

            elif medewerker.rol_id !=None and medewerker.functie_id == None:
                if medewerker.rol_id == role :
                    MedewerkerProfile.objects.filter(id=idmedewerker).update(functie_id=idfunctie)
                    return JsonResponse({
                        'is_success': True,
                        'message': str(medewerker) + ' is successvol toegevoegd',
                        })
                else:
                    return JsonResponse({
                        'is_success': False,
                        'message': str(medewerker) + ' hoort bij een role waar deze functie niet bijhoord',
                        })
            else:
                return JsonResponse({
                    'is_success': False,
                    'message': str(medewerker) + ' kan alleen een functie hebben'
                    })
        else:
            functie = Functie.objects.filter(id=id).get()
            functie_name = functie.functie
            functie_id = functie.id
            medewerkers = MedewerkerProfile.objects.filter(functie_id =id)
            return render(request, 'functie/functieoverzichtbewerken.html',{
                'medewerkers': medewerkers,
                'functie_id':functie_id,
                'functie_name': functie_name
            })
                
    except Exception as e:
        messages.success(request,str(e))
        return JsonResponse({"message":str(e)})

# @login_required
def functiemedewerkerverwijderen(request,id):
    if request.is_ajax():
        user_id = request.POST.get('idmedewerker')
        # role_id = request.POST.get('idrole')
        # medewerker = MedewerkerProfile.objects.filter(id=user_id).get()
        MedewerkerProfile.objects.filter(id=user_id).update(rol_id=None,functie_id=None)
        return JsonResponse({
            'is_success': True,
            'message': ' is successfuly uit de functie table verwijderd'
            })    
    else:
        return JsonResponse({
            'is_success': False,
            'message': 'something went wrong'
            })


@login_required
def klantoverzicht(response):
    klanten = KlantProfile.objects.all()
    return render(response, 'klant/klantoverzicht.html',{
       'klanten': klanten
    })

@login_required
def getNavbarData(request):
    if request.is_ajax():
        if request.method == 'POST':
            idUser = request.POST['id']
            user = MedewerkerProfile.objects.filter(user_id=idUser).get()
            if user.functie_id == None:
                functienaam = 'Functie onbekend'
            else:
                functie = Functie.objects.filter(id=user.functie_id).get()
                functienaam = functie.functie
    return JsonResponse({
        'functienaam':functienaam
    })
# profile overzicht
@login_required
def userprofile(request,id=None):
    if request.method == 'POST':
        password = request.POST['password']
        password_ = request.POST['password_']
        try:
            user = CustomUser.objects.get(id=id)
            if user.check_password(password):
               CustomUser.objects.filter(id=id).update(password = make_password(password_))
               messages.success(request,'Wactwoord is successfully updated,U moet opniew inloggen met de nieuwe wachtwoord om verder te kunnen gaan')
               return redirect('login')
            else:
                messages.success(request,'Oude password is niet correct')
                return render(request, 'userprofile/userprofile.html',{
                        'email': user.email,
                        'medewerker': MedewerkerProfile.objects.get(user_id=user.id),
                        'functies': Functie.objects.all(),
                        'roles': Role.objects.all()
                    })
        except Exception as e: 
            messages.success(request,str(e))
            return render(request, 'userprofile/userprofile.html',{
                'email': user.email,
                'medewerker': MedewerkerProfile.objects.get(user_id=user.id),
                'functies': Functie.objects.all(),
                'roles': Role.objects.all()
             }) 
    else:

        if id:
            user = get_object_or_404(CustomUser,id=id)
        else:
            id = request.user
            user = CustomUser.objects.get(id=id)
            

        return render(request, 'userprofile/userprofile.html',{
            'email': user.email,
            'medewerker': MedewerkerProfile.objects.get(user_id=user.id),
            'functies': Functie.objects.all(),
            'roles': Role.objects.all()
        })


# medewerkers overzicht
@login_required
def medewerkeroverzicht(request):
    medewerkers = MedewerkerProfile.objects.all()
    customusers = CustomUser.objects.all() 
    roles = Role.objects.all()
    functies = Functie.objects.all()

    return render(request, 'medewerker/medewerkersoverzicht.html',{
       'medewerkers': medewerkers,
       'customusers': customusers,
       'roles': roles,
       'functies': functies
    })

# def email_check(user):
#     user.email.endswitch('@factoryzero.nl')


@login_required
# @user_passes_test
def createmedewerker(request):
    if request.is_ajax() and request.method == "POST":
        email = request.POST['email']
        voornaam =request.POST['voornaam']
        voorletter = request.POST['voorletter']
        tussenvoegsel = request.POST['tussenvoegsel']
        achternaam = request.POST['achternaam']
        geslacht = request.POST['geslacht']
        geboortdatum = request.POST['geboortdatum']
        phone_no = request.POST['phone']
        password = request.POST['password']
        re_password = request.POST['re_password']
        is_staff = 1
        is_superuser = 0
        rol = request.POST['role']
        functie = request.POST['functie']
        try:
            if CustomUser.objects.filter(email=email).exists():
                return JsonResponse({
                    'is_success': False,
                    'message': str(email) + ' bestaal al'
                    })
            else:
                if password == re_password:
                    if len(password) < 8:
                        return JsonResponse({
                            'is_success': False,
                            'message': 'Wachtwoord moet tenmisnte 8 charachters zijn'
                            })
                    else:
                        user = CustomUser.objects.create(email = email,password = make_password(password),is_staff = is_staff,is_superuser=is_superuser)
                        if Role.objects.filter( id = rol).exists():
                            if Functie.objects.filter( id = functie).exists():
                                medewerker = MedewerkerProfile.objects.create(
                                        voornaam = voornaam,
                                        voorletter = voorletter,
                                        tussenvoegsel = tussenvoegsel,
                                        achternaam = achternaam,
                                        geslacht = geslacht,
                                        geboortdatum = geboortdatum,
                                        phone_no = phone_no,
                                        rol_id = rol,
                                        functie_id = functie,
                                        user_id = user.id,
                                        )
                                user.save()
                                medewerker.save()
                                return JsonResponse({
                                    'is_success': True,
                                    'message': voornaam + 'is successvol gemaakt'
                                    })
                            else:
                                return JsonResponse({
                                    'is_success': False,
                                    'message': 'functie moet eerste aangemaakt worden'
                                    })
                        else:
                            return JsonResponse({
                                'is_success': False,
                                'message': 'role moet eerste aangemaakt worden'
                                })
                            
                else:
                    return JsonResponse({
                        'is_success': False,
                        'message': 'Wactwoord komt niet overeen'
                        })

        except Exception as e:
            return JsonResponse({
                'is_success': False,
                'message': str(e)
                }) 
    else:
        if request.method == "POST":
            email = request.POST['email']
            voornaam =request.POST['voornaam']
            voorletter = request.POST['voorletter']
            tussenvoegsel = request.POST['tussenvoegsel']
            achternaam = request.POST['achternaam']
            geslacht = request.POST['geslacht']
            geboortdatum = request.POST['geboortdatum']
            phone_no = request.POST['phone']
            password = request.POST['password']
            re_password = request.POST['re_password']
            is_staff = 1
            is_superuser = 0
            rol = request.POST['role']
            functie = request.POST['functie']
            try:
                if CustomUser.objects.filter(email=email).exists():
                    messages.success(request,'Medewerker bestaat al')
                    return redirect('createmedewerker')
                else:
                    if password == re_password:
                        if len(password) < 8:
                            messages.success(request,'Wachtwoord moet meer dan 8 charachters zijn')
                            return redirect('createmedewerker')
                        else:
                            user = CustomUser.objects.create(email = email,password = make_password(password),is_staff = is_staff,is_superuser=is_superuser)
                            if Role.objects.filter( id = rol).exists():
                                if Functie.objects.filter( id = functie).exists():
                                    medewerker = MedewerkerProfile.objects.create(
                                            voornaam = voornaam,
                                            voorletter = voorletter,
                                            tussenvoegsel = tussenvoegsel,
                                            achternaam = achternaam,
                                            geslacht = geslacht,
                                            geboortdatum = geboortdatum,
                                            phone_no = phone_no,
                                            rol_id = rol,
                                            functie_id = functie,
                                            user_id = user.id,
                                            )
                                    user.save()
                                    medewerker.save()
                                    messages.success(request,'Medewerker is successvol gemaakt')
                                    return redirect('medewerkeroverzicht')
                                else:
                                    messages.success(request,'functie moet eerste aangemaakt worden')
                                    return redirect('createmedewerker')
                            else:
                                messages.success(request,'role moet eerste aangemaakt worden')
                                return redirect('createmedewerker')
                    else:
                        messages.success(request,'Wactwoord komt niet overeen')
                        return redirect('createmedewerker')

            except Exception as e: 
                messages.success(request,str(e))
                return redirect('createmedewerker')
        else:
            roles = Role.objects.all()
            functies = Functie.objects.all()
            return render(request, 'medewerker/createmedewerker.html',{
                'roles': roles,
                'functies': functies
            }) 

        

@login_required
def medewerkerbewerken(request,id):
    
    medewerkerobj = MedewerkerProfile.objects.get(id=id)
    roleobj = Role.objects.all()
    functieobj = Functie.objects.all()
    user = CustomUser.objects.filter(id=medewerkerobj.user_id).get()
    mewerkeremail = user.email

    if request.is_ajax():
        if request.method == 'POST':
            voornaam = request.POST['voornaam']
            voorletter = request.POST['voorletter']
            tussenvoegsel = request.POST['tussenvoegsel']
            achternaam = request.POST['achternaam']
            geslacht = request.POST['geslacht']
            role = request.POST['role']
            functie = request.POST['functie']

            if request.POST['geboortdatum']:
                geboortdatum = request.POST['geboortdatum']
            else:
                geboortdatum = medewerkerobj.geboortdatum

            if request.POST['geslacht']:
                geslacht = request.POST['geslacht']
            else:
                geslacht = medewerkerobj.geslacht

            phone = request.POST['phone']
            try:
                MedewerkerProfile.objects.filter(id=id).update(
                    voornaam=voornaam,
                    voorletter=voorletter,
                    tussenvoegsel=tussenvoegsel,
                    achternaam=achternaam,
                    geslacht=geslacht,
                    rol_id=role,
                    functie_id=functie,
                    geboortdatum=geboortdatum,
                    phone_no=phone
                    )
                
                return JsonResponse({
                    'is_success': True,
                    'message': 'Medewerker is successvol bewerkt'
                })
                
            except Exception as e: 
                return JsonResponse({
                    'is_success': False,
                    'message': str(e)
                })
              

        else:
            return render(request,'medewerker/medewerkerbewerken.html',{
                'medewerkerobj': medewerkerobj,
                'roleobj': roleobj,
                'functieobj': functieobj,
                'medewerkeremail': mewerkeremail
            })
    else:
        return render(request,'medewerker/medewerkerbewerken.html',{
                'medewerkerobj': medewerkerobj,
                'roleobj': roleobj,
                'functieobj': functieobj,
                'medewerkeremail': mewerkeremail
            })




@login_required
def create_user(request):
    if request.method == "POST":
        email = request.POST['email']
        is_staff = request.POST['is_staff']
        voornaam =request.POST['voornaam']
        voorletter = request.POST['voorletter']
        tussenvoegsel = request.POST['tussenvoegsel']
        achternaam = request.POST['achternaam']
        geslacht = request.POST['geslacht']
        geboortdatum = request.POST['geboortdatum']
        phone_no = request.POST['phone']
        password = request.POST['password']
        re_password = request.POST['re_password']
        try:
            if CustomUser.objects.filter(email=email).exists():
                messages.success(request,'Gebruiker bestaat al')
                return redirect('register')
            else:
                if password == re_password:
                    if len(password) < 8:
                        messages.success(request,'Wachtwoord moet meer dan 8 charachters zijn')
                        return redirect('register')
                    else:
                        user = CustomUser.objects.create(email = email,password = make_password(password),is_staff = is_staff)
                        if is_staff == "False":
                            is_particulier = request.POST['is_particulier']
                            klant = KlantProfile.objects.create(
                                voornaam = voornaam,
                                voorletter = voorletter,
                                tussenvoegsel = tussenvoegsel,
                                achternaam = achternaam,
                                geslacht = geslacht,
                                geboortdatum = geboortdatum,
                                phone_no = phone_no,
                                is_particulier = is_particulier,
                                user_id = user.id
                            )
                            klant.save()
                            messages.success(request,'Klant is met success aangemaakt',is_staff)
                            return redirect('klantoverzicht')
                        else:
                            rol = request.POST['role']
                            functie = request.POST['functie']
                            if Role.objects.filter( id = rol).exists():
                                if Functie.objects.filter( id = functie).exists():
                                    medewerker = MedewerkerProfile.objects.create(
                                        voornaam = voornaam,
                                        voorletter = voorletter,
                                        tussenvoegsel = tussenvoegsel,
                                        achternaam = achternaam,
                                        geslacht = geslacht,
                                        geboortdatum = geboortdatum,
                                        phone_no = phone_no,
                                        rol_id = rol,
                                        functie_id = functie,
                                        user_id = user.id,
                                        )
                                    medewerker.save()
                                    messages.success(request,'Medewerker is successvol gemaakt')
                                    return redirect('medewerkeroverzicht')
                                else:
                                    messages.success(request,'functie moet eerste aangemaakt worden')
                                    return redirect('register')
                            else:
                                messages.success(request,'role moet eerste aangemaakt worden')
                                return redirect('register')

                else:
                    messages.success(request,'Wactwoord komt niet overeen')
                    return redirect('register')
        except Exception as e: 
            messages.success(request,str(e))
            return redirect('register')
    else:
        roles = Role.objects.all()
        functies = Functie.objects.all()
        return render(request, 'register/register.html',{
            'roles': roles,
            'functies': functies
        }) 


# KLANT CREATE
def klantcreate(request):
    if request.is_ajax() and request.method == "POST":
        voornaam = request.POST['voornaam']
        voorletter = request.POST['voorletter']
        tussenvoegsel = request.POST['tussenvoegsel']
        achternaam = request.POST['achternaam']
        geslacht = request.POST['geslacht']
        geboortdatum = request.POST['geboortdatum']
        phone_no = request.POST['phone_no']
        # fax_number = request.POST['fax_number']
        is_particulier = request.POST['is_particulier']
        email = request.POST['email']
        try:
            if KlantProfile.objects.filter(email=email).exists():
                return JsonResponse({
                    'is_success': False,
                    'msg': 'Klant bestaat al'
                })
            else:
                KlantProfile.objects.create(email=email,voornaam=voornaam,voorletter=voorletter,tussenvoegsel=tussenvoegsel,
                    achternaam=achternaam,geslacht=geslacht,geboortdatum=geboortdatum,phone_no=phone_no,is_particulier=is_particulier)
                return JsonResponse({
                    'is_success': True,
                    'msg': voornaam + ' klant is successvol aangemaakt'
                    
                })
        except Exception as e:
            return JsonResponse({
                'is_success': False,
                'msg': str(e)
            })

    else:
        return render(request,'klant/createklant.html',{})


def login_excluded(redirect_to):
    """ This decorator kicks authenticated users out of a view """ 
    def _method_wrapper(view_method):
        def _arguments_wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect(redirect_to) 
            return view_method(request, *args, **kwargs)
        return _arguments_wrapper
    return _method_wrapper

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

# login user
@login_excluded('home')
def login_user(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate_user(email=email, password=password)
        try:
                if user is not None:   
                    login(request, user)
                    if user.is_active !=1:
                        user.is_active = 1
                        user.last_login = dateformat.format(timezone.now(), 'Y-m-d H:i:s')
                        user.save()
                    medewerker = MedewerkerProfile.objects.filter(user_id=user.id).get()
                    voornaam = medewerker.voornaam
                    request.session['voornaam'] = voornaam
                    request.session['achternaam'] = medewerker.achternaam
                    messages.success(request,'welkom')
                    return redirect('home')
                else:
                    # Return an 'invalid login' error message.
                    messages.success(request,'Wrong Email or Passowrd. Please try again')
                    return redirect('login')
        except:
            messages.success(request,'Gebruiker bestaat niet. Neem contact met de admin van de website')
            return redirect('login')
    else:
        return render(request, 'register/login.html',{})

@login_required
def home(request):
    return render(request,'home/home.html',{})

@login_required
def logout_user(request):
    user = request.user
    user.is_active = 0
    user.save()
    logout(request)
    messages.success(request,'You are logged out',user.is_active)
    return redirect('login')