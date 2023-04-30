import json
from multiprocessing import context
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from datetime import date,datetime
from django.core import serializers
from countryinfo import CountryInfo
from .serializer import ProjectIcemSerializer,ProjectSerializer,KlantSerializer,KlantMedewerkerSerializer
from .models import Project,ProjectIcem,Vertegenwoordiger_Project,KlantMedewerker,Klant,Onderaanemerbedrijf,StatusOnderaanemer
from mpo.models import Site,Icem
from users.models import MedewerkerProfile,klantWoningbouw,Role,Functie,CustomUser
from users.serializers import MedewerkerSerializer,klantWoningbouwSerializer
import numpy as np
# GET DATEFORMAT

# GET LAND
def getLandNaam(self,string):

    if string == 'Nederland':
       return 'Nederland' 
    elif string == 'England':
        return 'England'
    else:
        return ''

 # GET KLANTNAAM
def getKlantNaam(self,id):
   
    klant = Klant.objects.filter(id=id).get()
    klantnaam = klant.klantnaam
    return klantnaam
def projectleiderFZArray(string):
    # GET FUNCTIES
    functies = Functie.objects.values_list('id','functie')
    customers = []
    users = []
    
    for i in functies:   
        if i[1] == string:
            customers = CustomUser.objects.filter(functie_id = i[0]).values_list('id')
        else:
            pass

    for i in customers:
        medewerker = MedewerkerProfile.objects.filter(user_id = i[0]).get()
        medewerkerObject = {
            'id': medewerker.id,
            'name': medewerker.voornaam + ' ' + medewerker.achternaam,
            'phone_no':str(medewerker.phone_no)
        }
        users.append(medewerkerObject)
    return users
def returnProvinciesperLand(country):
    country_= CountryInfo(country)
    provincies = country_.provinces()
    return provincies

def getKlanten():
    klanten = Klant.objects.values_list('id','klantnaam')

    return klanten
# UPDATE PROJECT
class UpdateProject(APIView):
    def getMedewerkerId(self,id):
        project = Project.objects.filter(id=id).get()
        return project.klant_id
    def get_onderaanemer(self,param):
        onderaanemer = Onderaanemerbedrijf.objects.get(id=int(param))
        return onderaanemer
    def check_datas_to_be_sent(self,param1,param2,param3,param4):
        data_to_be_sent = {
                'status': param1,
                'odernummer': param3,
                'onderaanemer': self.get_onderaanemer(param2),
                'project_id': param4
            }

        try:
            if StatusOnderaanemer.objects.filter(project_id=data_to_be_sent['project_id'],onderaanemer=data_to_be_sent['onderaanemer'],status=data_to_be_sent['status']).exists():
                StatusOnderaanemer.objects.filter(project_id=data_to_be_sent['project_id'],onderaanemer=data_to_be_sent['onderaanemer'],status=data_to_be_sent['status']).update(**data_to_be_sent)
                return True
            else:
                StatusOnderaanemer.objects.create(**data_to_be_sent)
                return True  
        except Exception as e:
            return str(e)
        

    def createOrupdateStatusOnderaanemer(self,project,data):
        for key, value in data.items(): 
           
            if key == 'inopdrachtvoor_vloerverwarming':
                if data['inopdrachtvoor_vloerverwarming'] != None:
                    res = self.check_datas_to_be_sent('vloerverwarming',data['inopdrachtvoor_vloerverwarming'],data['ordernr_onderaannemer_vloerverwarming'],project)
                    return res
                else:
                    return None
                
            elif key == 'inopdrachtvoor_ventilatieinstallatie':
                if data['inopdrachtvoor_ventilatieinstallatie'] != None:
                    res = self.check_datas_to_be_sent('ventilatieinstallatie',data['inopdrachtvoor_ventilatieinstallatie'],data['ordernr_onderaannemer_vloerverwarming'],project)
                    return res
                else:
                    return None
            elif key == 'inopdrachtvoor_zonnepanelen':
                if data['inopdrachtvoor_zonnepanelen'] != None:
                    res = self.check_datas_to_be_sent('zonnepanelen',data['inopdrachtvoor_zonnepanelen'],data['ordernr_onderaannemer_zonnenpanelen'],project)
                    return res
                else:
                    return None
            else:
                return None
    def post(self,request,format=None):
        data = self.request.data
        projectdata = data['project_data']
        if data:
            try:
                Project.objects.filter(projectnr=projectdata['projectnr']).update(**projectdata)
                project = Project.objects.get(projectnr=projectdata['projectnr'])
                try:
                    self.createOrupdateStatusOnderaanemer(project,data['aanemers_data'])
                    return Response({ 'success': 'project met success bijewerkt'})
                except Exception as e:
                    return Response({ 'error': str(e)})
            except Exception as e:
                print(e)
                return Response({'error': str(e)})


# GET ALL PROJECTS
class AllProjectsList(APIView):
    def get(self,request,format=None):
        try:

            projects = Project.objects.values('id','projectnaam','projectnr')
            return Response({
            'data': projects,
        })
        except Exception as e:

            return Response({
                'error': str(e)
            })

# GET ALL PROJECTVIEW

class GetAllProjects(APIView):
    klantnameObject = getKlantNaam
    landObject = getLandNaam
    # dateformat = getDateformat

    def getIcemType(self,projectID):
        icemTypes = []
        
        for site in Site.objects.filter(projectId_id=projectID):
            icemType = Icem.objects.filter(site=site).get() 
            if icemType == None:
                pass
            else:
                icemTypes.append(icemType.icemType)
        return icemTypes
    def checkIfIcemTypeexist(self,icemData,typeIcem):
        icemTypeArray = []
        
        for i in icemData:
            if i == typeIcem:
                icemTypeArray.append(i)
            else:
                pass
        return len(icemTypeArray)

    def get(self,request,format=None):
        # ids = list(your_queryset.values_list('content_id', flat=True))
        # projects = Project.objects.in_bulk(ids)
        projects = Project.objects.all()
        
        projectContext = []

        for project in projects:
            projectnr = project.projectnr
            icemTypesperproject = self.getIcemType(project.id)
            
            i = self.checkIfIcemTypeexist(icemTypesperproject,"i")
            p = self.checkIfIcemTypeexist(icemTypesperproject,"p")
            e = self.checkIfIcemTypeexist(icemTypesperproject,"e")
            f = self.checkIfIcemTypeexist(icemTypesperproject,"f")
            a = self.checkIfIcemTypeexist(icemTypesperproject,"a")
            sum = i+p+e+f+a

            object = {
                'id': project.id,
                'projectnr': projectnr,
                'klantnaam': self.klantnameObject(project.klant_id),
                'renovatie_nieuwbouw': project.renovatie_nieuwbouw,
                'projectstatus': project.projectStatus,
                'projectnaam':project.projectnaam,
                'sum':sum,
                'i':i,
                'p':p,
                'e':e,
                'f':f,
                'a':a,
                'something':0,
                'afgifte_opwek': '-',
                'energie_prestatie_garantie':'ja',
                'plaats': project.plaats,
                'provincie':project.provincie,
                'land': self.landObject(project.land),
                'projectsom': '#',
                'datum_systeem_invoer': project.datumSystemInvoer,
                'startdatum': project.startDatum,
                'offertedatum': project.offertedatum
            }
            projectContext.append(object)
        return Response({
            'data': projectContext
            })


# CREATE KLANT VIEW
class CreateKlant(APIView):
    def post(self, request, format=None):
        data = self.request.data
        klantnaam = data['klant_naam']
        plaatsklant = data['plaatsklant']
        phoneklant = data['phoneklant']
        provincie_ = data['provincieKlant']
        land_ = data['landklant']
       
        try:
            klant = Klant.objects.create(klantnaam=klantnaam,plaats=plaatsklant,land=land_,provincie = provincie_,phone=phoneklant)
            klant.save()
            return Response({'success': klantnaam + 'is successful aangemaakt'})
        except Exception as e:
            return Response({'error': str(e)})

# CREATE ONDERAANEMER VOOR
class CreateOnderaanemer(APIView):
    def post(self,request,format=None):
        data = self.request.data
        onderaanemerObject = {
            'naam': data['naam'],
        }
     
        try:
            onderaanemer  = Onderaanemerbedrijf.objects.create(**onderaanemerObject)
            onderaanemer.save() 
            return Response({'success': True})
        except Exception as e:
            return Response({'error': str(e)})

class ListOnderaanemer(APIView):
    def get(self,request,format=None):
        data = Onderaanemerbedrijf.objects.values_list('id','naam')
        return Response({'data': data})

# CREATE MEDEWERKER KLANT VIEW
class CreateKlantMedewerkerView(APIView):
    def post(self, request, format=None):
        data = self.request.data
        klantId = data['klantID_id']
        jsonData = {
            'name_medewerker': data['name_medewerker'],
            'achternaam_medewerker': data['achternaam_medewerker'],
            'phone': data['phone'],
            'functie_medewerker': data['functie_medewerker'],
            'klantID_id': klantId
        }
   
        try:
            if KlantMedewerker.objects.filter(klantID_id=klantId,functie_medewerker=data['functie_medewerker']).exists():
                KlantMedewerker.objects.filter(klantID_id=klantId,functie_medewerker=data['functie_medewerker']).update(**jsonData)
                return Response({'success': data['name_medewerker'] + 'is successful bijgewerkt'})
            else:
                klantMedeweker = KlantMedewerker.objects.create(**jsonData)
                klantMedeweker.save()
                return Response({'success': data['name_medewerker'] + 'is successful aangemaakt','projectid': data['projectid']})
        except Exception as e:
            return Response({'error': str(e)})

class GetProjectDataVoorBewerken(APIView):
    def getProjectdatas(self,id):
        try:

            project_data = Project.objects.filter(id=id).values('id','projectnr','projectnaam','plaats','provincie','land','projectStatus','offertenr','exactnr','debiteurnr','renovatie_nieuwbouw','inopdrachtvoor_vloerverwarming','inopdrachtvoor_ventilatieinstallatie','inopdrachtvoor_zonnepanelen','datumSystemInvoer','startDatum','klant_id','offertedatum','uitlijkDatumOpdrachtIndienWTW','uitlijkDatumOpdrachtAlleenICEM','opmerking')
            return project_data[0]
        except Exception as e:
            return str(e)
    def getKlantId(self,id):
        try:
            idKlant = Project.objects.filter(id=id).values('klant_id')
            return idKlant[0]['klant_id']
        except Exception as e:
            return str(e)
    def getKlantNaam(self,id):
        try:
            klant = Klant.objects.filter(id=id).values('id','klantnaam')
            return klant[0]
        except Exception as e:
            return str(e)
    def getContactpersonFZ(self,id):
        try:
            contactpersonen  = Project.objects.filter(id=id).values('selectedWerkvoorbereiderFz','selectedProjecleiderFz')
           
            return contactpersonen[0]
        except Exception as e:
            return str(e)

    def getMedewerkerFz(self,id):
        try:
            if id != None:
                medewerker = MedewerkerProfile.objects.filter(id=int(id)).values('id','voornaam','achternaam','phone_no')
                return medewerker[0]
            else:
                return None
        except Exception as e:
            return str(e)
    def getInopdrachtVoor(self,id):
        try:
            inOpdrachten = Project.objects.filter(id=id).values('inopdrachtvoor_vloerverwarming','inopdrachtvoor_ventilatieinstallatie','inopdrachtvoor_zonnepanelen')
            return inOpdrachten[0]
        except Exception as e:
            return str(e)

    def check_if_is_inopdracht_voor_fz(self,id,string,status):
        if string == 'FZ':
            ondernemerProjectStatus = StatusOnderaanemer.objects.filter(project_id_id=id,status = status).values('odernummer','onderaanemer_id')
            aanemer = Onderaanemerbedrijf.objects.filter(id=ondernemerProjectStatus[0]['onderaanemer_id']).values('id')
            return {'aanemer': aanemer[0],'odernr':ondernemerProjectStatus[0]['odernummer']}
        elif string == "Derden":
            return {'inopdrachtvoor': 'Derden','aanemer': None}
        else:
            return {'inopdrachtvoor': None,'aanemer': None}

    def get_contactpersonklant(self,idklant,functie):
        try:
            if KlantMedewerker.objects.filter(klantID_id=idklant,functie_medewerker=functie).exists():
              klantmedewerker = KlantMedewerker.objects.filter(klantID_id=idklant,functie_medewerker=functie).values('name_medewerker','achternaam_medewerker','phone')
              return klantmedewerker[0]
            else:
                return None
        except Exception as e:
            return str(e)
    def get_medewerkers_by_functie(self,string):
        medewerkers = []
        try:
            if Functie.objects.filter(functie=string).exists():
                functie = Functie.objects.get(functie=string) 
            else:
              functie = None 
        except Exception as e:
            print(e)
            return str(e)
        try:
            if functie == None:
                return None
            else:

                user = CustomUser.objects.filter(functie=functie)
            
                if len(user) > 0:
                    
                    for i in user:
                        medewerker = MedewerkerProfile.objects.filter(user=i).values('id','voornaam','achternaam','phone_no')
                        medewerkers.append(medewerker[0])
              
            return medewerkers
        except Exception as e:
            print(e)
            return str(e)

    def post(self,request,format=None):
        id = self.request.data
        projectdata = self.getProjectdatas(id)
        klant = self.getKlantNaam(self.getKlantId(id))
        
        contactpersonenFz = self.getContactpersonFZ(id)
  
        projectleiderFz = self.getMedewerkerFz(contactpersonenFz['selectedProjecleiderFz'])
        werkvoorbereiderFz = self.getMedewerkerFz(contactpersonenFz['selectedWerkvoorbereiderFz'])
        inOpdrachten = self.getInopdrachtVoor(id)
        inOpdrachtendata = {
            'afgiftesystem': self.check_if_is_inopdracht_voor_fz(id,inOpdrachten['inopdrachtvoor_vloerverwarming'],'vloerverwarming'),
            'ventillatie': self.check_if_is_inopdracht_voor_fz(id,inOpdrachten['inopdrachtvoor_ventilatieinstallatie'],'ventilatieinstallatie'),
            'zonnepanelen': self.check_if_is_inopdracht_voor_fz(id,inOpdrachten['inopdrachtvoor_zonnepanelen'],'zonnepanelen'),
        }
        # countries cities
        provincies = {
            'nl':returnProvinciesperLand('Nederland'),
            'en': returnProvinciesperLand('Uk')
        }
        jsoncontactpersonenklanten = {
            'projectleiderklantmedeweker':  self.get_contactpersonklant(klant['id'],'Projectleider'),
            'werkvoorbereiderklantmedeweker':  self.get_contactpersonklant(klant['id'],'Werk-voorbereider'),
            'uitvoerderklantmedeweker':  self.get_contactpersonklant(klant['id'],'Uitvoerder'),
        }
        jsoncontactpersonenfz = {
            'projectleiderFz': projectleiderFz,
            'werkvoorbereiderFz': werkvoorbereiderFz,
        }
        jsonmedewerkerFz = {
            'projectleiders': self.get_medewerkers_by_functie('Projectleider'),
            'werkvoorbereiders': self.get_medewerkers_by_functie('Werkvoor-bereider')
        }
        jsondata = {
            'projectdata': projectdata,
            'klant': klant,
            'contactpersonKlant': jsoncontactpersonenklanten,
            'contactpersonFz': jsoncontactpersonenfz,
            'medewerkersfz': jsonmedewerkerFz,
            'inOpdrachten': inOpdrachtendata,
            'provincies': provincies
        }
        return Response(
            {
            'data': jsondata
            }
        
        ) 

class BewerkenKlantMedeweker(APIView):
    def post(self,request,format=None):
        data = self.request.data
        flushData = {
            'name_medewerker': data['name_medewerker'],
            'achternaam_medewerker': data['achternaam_medewerker'],
            'phone': data['phone'],

        }
        try:
            KlantMedewerker.objects.filter(klantID_id = data['klantID_id'],functie_medewerker=data['functie_medewerker']).update(**flushData)
            return Response({'success': True})
        except Exception as e:
            return Response({ 'error': str(e)})
    
class GetProjectById(APIView):

    project_class = ProjectSerializer
    klantnameObject = getKlantNaam
    # GET ALL PROJECT OBJECT
    def get_queryset(self,id):
            if Project.objects.filter(id=id).exists():

                project = Project.objects.filter(id=id).get()
                return project
            else:
                project = None

    # GET WERKVOORBEREIDER Aanemer
    def getWerkVoorbereiderAanemer(self,id):
       
        if id !=0 and id is not None:
            werkvoorbereiderAanemer = KlantMedewerker.objects.filter(id=id).get()
            werkvoorberediderAanemerserializer = {
                'name': werkvoorbereiderAanemer.name_medewerker,
                'phone': werkvoorbereiderAanemer.phone
            }

            return werkvoorberediderAanemerserializer
        else:
            return None

    # GET Project Leider Aanemer
    def getProjectleiderAanemer(self,id):
        if id !=0 and id is not None:
            projectleiderAanemer = KlantMedewerker.objects.filter(id=id).get()
            projectleideraanemerserializer = {
                'name':projectleiderAanemer.name_medewerker,
                'phone': projectleiderAanemer.phone
            }
            return projectleideraanemerserializer
        else:
            return None
    
    # GET UITVOERDER Aanemer
    def getUitvoerderAanemer(self,id):
        if id !=0 and id is not None:
            uitvoerderAanemer = KlantMedewerker.objects.filter(id=id).get()
            uitvoerderAanemerserializer = {
                'name':uitvoerderAanemer.name_medewerker,
                'phone': uitvoerderAanemer.phone
            }
            return uitvoerderAanemerserializer
        else:
            return None

    # GET WERKVOORBEREIDER FZ
    def getWerkvoorbereiderFZ(self,id):
     
        if id !=0 and id is not None:
            werkvoorbereiderFZ = MedewerkerProfile.objects.filter(id=id).get()
            werkvoorbereiderFZserializer = {
                'name':werkvoorbereiderFZ.voornaam + ' '+werkvoorbereiderFZ.achternaam,
                'phone': str(werkvoorbereiderFZ.phone_no)
            }
            return werkvoorbereiderFZserializer 
        else:
            return {}
    
     # GET PROJECTLEIDER FZ

    def getProjectleiderFZ(self,id):
        if id !=0 and id is not None:
            projectleiderFZ = MedewerkerProfile.objects.filter(id=id).get()
            projectleiderFZserializer = {
                'name':projectleiderFZ.voornaam + '  '+ projectleiderFZ.achternaam,
                'phone': str(projectleiderFZ.phone_no)
            }
            return projectleiderFZserializer
        else:
            return {}

    def return_installatieComponenten(self,args):
        value = ''
        if args is not None:
            print(args)
        else:
            value = None
        return value

    def return_bedrijfsaanemers(self):
        res = Onderaanemerbedrijf.objects.values('id','naam')
        return res

    def get_klant_medewerker(self,id,string):
        if KlantMedewerker.objects.filter(klantID_id=id,functie_medewerker=string).exists():
            res = KlantMedewerker.objects.filter(klantID_id=id,functie_medewerker=string).get()
            jsonresponse = {'id': res.id,'naam':res.name_medewerker + ' ' + res.achternaam_medewerker,'phone': res.phone}
            return jsonresponse
        else:
            return None

    def checkifIsnotNone(self,value):
        if value == None:
            return None
        else: 
            return value
    
    def post(self,request, *args,**kwargs):

        data = self.request.data
        project = self.get_queryset(data)
        projectnummer = ''   
        klantnaam = ''
        projectnaam = ''
        plaats = ''
        provincie = ''
        projectstatus = ''
        werkVoorbereiderAanemer = ''
        uitvoerderAanemer = ''
        projectleiderAanemer = ''
        werkVoorbereiderFZ = ''
        projectleiderFZ = ''
        contextprojectbewerken = []
        
        provincies = {
            'nl': returnProvinciesperLand('Nederland'),
            'en': returnProvinciesperLand('Uk')
        }

        if project != None:
            projectnummer = project.projectnr
            klantnaam = self.klantnameObject(project.klant_id)
            projectnaam = project.projectnaam
            plaats = project.plaats
            provincie = project.provincie
            projectstatus = project.projectStatus
            werkVoorbereiderFZ = self.getWerkvoorbereiderFZ(project.selectedWerkvoorbereiderFz)
            projectleiderFZ = self.getProjectleiderFZ(project.selectedProjecleiderFz)
            projecleiderAanemer_ = self.get_klant_medewerker(project.klant_id,'Projectleider')
            werknemerAanemer_ = self.get_klant_medewerker(project.klant_id,'Werk-voorbereider')
            uitvoerderAanemer_ = self.get_klant_medewerker(project.klant_id,'Uitvoerder')
         
            contextprojectbewerken = {
                'projectnummer': projectnummer,
                'projectnaam': projectnaam,
                'plaats': project.plaats,
                'klantID': project.klant_id,
                'provincie': project.provincie,
                'land': project.land,
                'projectstatus': project.projectStatus,
                'provincies':provincies,
                'klantnaam': klantnaam,
                'offetenummer': project.offertenr,
                'exactnummer': project.exactnr,
                'debiteurnummer': project.debiteurnr,
                'renovatie_nieuwbouw': project.renovatie_nieuwbouw,
                'projectleiderAanemer': projecleiderAanemer_,
                'werkVoorbereiderAanemer': werknemerAanemer_,
                'uitvoerderAanemer': uitvoerderAanemer_,
                'projectleiderFZname': projectleiderFZ.get('name', ""),
                'projectleiderFzphone':projectleiderFZ.get('phone', ""),
                'projectleiderFzArray': projectleiderFZArray('Projectleider'), 
                # 'werkVoorbereiderFZ': werkVoorbereiderFZ,
                'werkvoorbereiderFZname': werkVoorbereiderFZ.get('name', ""),
                'werkvoorbedreiderFZphone':werkVoorbereiderFZ.get('phone', ""),
                'werkVoorbereiderFzArray': projectleiderFZArray('Werkvoor-bereider'),
                'inopdrachtAfgifteSystem': project.inopdrachtvoor_vloerverwarming,
                'afgifte_systeem': self.return_installatieComponenten(project.inopdrachtvoor_vloerverwarming),
                'ordernr_numerafgiftesystem': 1,
                'inopdrachtvoorventillatie': project.inopdrachtvoor_ventilatieinstallatie,
                'ventilatieinstallatie': self.return_installatieComponenten(project.inopdrachtvoor_ventilatieinstallatie),
                'ordernr_ventilatieinstallatie': 1,
                'inopdrachtvoorzonnepanelen': project.inopdrachtvoor_zonnepanelen,
                'zonnepanelen': self.return_installatieComponenten(project.inopdrachtvoor_zonnepanelen),
                'ordernr_zonnepanelen': 1,
                'aanemerbedrijven': self.return_bedrijfsaanemers(),
                'datumSystemInvoer': project.datumSystemInvoer,
                'startDatum': project.startDatum,
                'offertedatum': project.offertedatum,
                'uitlijkDatumOpdrachtIndienWTW': project.uitlijkDatumOpdrachtIndienWTW,
                'uitlijkDatumOpdrachtAlleenICEM': project.uitlijkDatumOpdrachtAlleenICEM,
                'opmerking': project.opmerking
            }
        context = {
            'projectnummer': projectnummer,
            'Klantnaam': klantnaam,
            'projectnaam': projectnaam,
            'plaats': plaats,
            'provincie': provincie,
            'projectstatus': projectstatus,
            'werkVoorbereiderAanemer': werkVoorbereiderAanemer ,
            'uitvoerderAanemer': uitvoerderAanemer,
            'projectleiderAanemer': projectleiderAanemer,
            'werkVoorbereiderFZ': werkVoorbereiderFZ,
            'projectleiderFZ': projectleiderFZ,
            'contextprojectbewerken': contextprojectbewerken,

        }
        return Response({'dataprojectbyID': context})

# @method_decorator(permission_required("project.add_project"), name='dispatch')
class CreateProjectView(APIView):

    def return_array_of_objects_status_onderaanemer(self,kwargs):
        arraobject = []
        for i in kwargs:
            if i['onderaanemer_id'] == '':
                pass
            else:
                arraobject.append({'status':i['status'],'onderaanemer_id':i['onderaanemer_id'],'odernummer':i['odernummer'],'project_id_id':i['project_id_id']})

        return arraobject
    def return_date_string_format(self,stringDate):
        # dateformat = None
        if stringDate != None and stringDate !='NaN-NaN-NaN' and stringDate != "01-01-1970":
            dateformat = datetime.strptime(stringDate, '%d-%m-%y')
            return dateformat
        else:
            dateformat = "01-01-1970"
            return dateformat

       
    def post(self, request, format=None):
        if(self.request.data):
            data = self.request.data
            # PROJECT OBJECT
            projectObject = {
                'projectnr':data['projectnr'],
                'projectnaam':data['projectnaam'],
                'plaats':data['plaats'],
                'provincie':data['provincie'],
                'land':data['land'],
                'projectStatus':data['projectStatus'],
                'offertenr':data['offertenr'],
                'exactnr':data['exactnr'],
                'debiteurnr':data['debiteurnr'],
                'renovatie_nieuwbouw':data['renovatie_nieuwbouw_'],
                'selectedWerkvoorbereiderFz': data['selectedWerkvoorbereiderFz'],
                'selectedProjecleiderFz': data['selectedProjecleiderFz'],
                'inopdrachtvoor_vloerverwarming': data['inopdrachtvoor_vloerverwarming'],
                'inopdrachtvoor_ventilatieinstallatie': data['inopdrachtvoor_ventilatieinstallatie'],
                'inopdrachtvoor_zonnepanelen': data['inopdrachtvoor_'],
                'datumSystemInvoer': data['system_datum_invoer'],
                'startDatum': data['startDatum'],
                'klant_id': data['selectedKlanten'],
                'offertedatum':data['offerteDatum'],
                'uitlijkDatumOpdrachtIndienWTW': data['uitlijk_datum_opdracht_indien_wtw'],
                'uitlijkDatumOpdrachtAlleenICEM': data['uitlijk_datum_opdracht_alleen_icem'],
                'opmerking': data['opmerking']
            }
  

            try:
                if data['projectnr'] != None:
                    # create project
                    project =  Project.objects.create(**projectObject)
                    project.save()
                    id = project.id
                    print(id)
                    try:
                        # Create the relatie tussen ondernemers en project
                        # CHECKIFONDERAANEMER IS None if not return array of objects
                      
                        objectofelementOnderaanemer =[ 
                            {'status': 'vloerverwarming','onderaanemer_id': data['onderaannemers_vloerverwarming'],'odernummer':data['ordernr_onderaannemer_vloerverwarming'],'project_id_id': id},
                            {'status': 'ventilatieinstallatie','onderaanemer_id': data['onderaannemers_ventilatieinstallatie'],'odernummer':data['ordernr_onderaannemer_ventilatieinstallatie'],'project_id_id': id},
                            {'status': 'zonnepanelen','onderaanemer_id': data['onderaannemers_'],'odernummer':data['ordernr_onderaannemer'],'project_id_id': id},
                        ]
                       
                        
                        statusonderaanmerObject = self.return_array_of_objects_status_onderaanemer(objectofelementOnderaanemer)
                     
                        if len(statusonderaanmerObject) != 0:
                            for i in statusonderaanmerObject:
                                statusonderaanemer = StatusOnderaanemer.objects.create(**i)
                                statusonderaanemer.save()
                        else:
                            pass
                       
                        return Response({'success': 'Project met success aangemaakt'})
                    except Exception as e:
                        return Response({'error': str(e)})
                else:
                    return Response({'error': 'Something went wrong'})
            except Exception as e:
   
                return Response({
                    'error': str(e)
                })

        
class GetProjectItems(APIView):

    
    def returnprojectnr(self,args):
        newprojectnr_ = str(int(args[2:]) + 1).zfill(3)
        return newprojectnr_ 

    def projectnr(self):
        projectnr = ''
        projectnrobj = Project.objects.last()
        if projectnrobj == None:
            projectnr = '001'
        else:
            projectnr_ = projectnrobj.projectnr
            projectnr = self.returnprojectnr(projectnr_)
        return projectnr

    def getMedewerkersperFunctie(self,functienaam):
        try:
            if Functie.objects.filter(functie=functienaam).exists():
                functie = Functie.objects.filter(functie=functienaam).values_list('id')
                users = CustomUser.objects.filter(functie_id=functie[0]).values_list('id')
                medewerkers = []
                for i in users:
                    medewerker = MedewerkerProfile.objects.filter(user_id = i[0]).values_list('id','voornaam','achternaam','phone_no')
                    result = {'id': medewerker[0][0],'voornaam':medewerker[0][1],'achternaam':medewerker[0][2],'phone_no':str(medewerker[0][3])}
                    medewerkers.append(result)
                    
                return medewerkers
        # list2 = [ids for ids in list]
            else:
                return None
        except Exception as e:
            print(e)
            return 'something wrong'
            
        
        
    def get(self, request, format=None):
        # medewerkers
        medewerkersqs = MedewerkerProfile.objects.all()
        medewerkers = MedewerkerSerializer(medewerkersqs,many=True)

        user = self.request.user
        # functie = Functie.objects.get(id=user.functie_id)

        # klant medewerkers
        # check if klantMederkerexist

        klantMedewerkersqs = KlantMedewerker.objects.all()
        # klantMedewerkers = KlantMedewerkerSerializer(klantMedewerkersqs,many=True)

        # klanten
        klantqs = Klant.objects.all()
        klant = KlantSerializer(klantqs,many=True)


        projectnr = self.projectnr()
        
        # ProjectLeiders aanemers
        def returnProjectleidersAanemers():
            projectleiders = []
            for projectleider in klantMedewerkersqs.iterator():
                if projectleider.functie_medewerker == "Projectleider":
                    result = {'id': projectleider.id,'voornaam':projectleider.name_medewerker,'achternaam':projectleider.achternaam_medewerker,'phone_no':str(projectleider.phone),'klantID': projectleider.klantID_id}
                    projectleiders.append(result)
            return projectleiders

        # Voorberediers aanemers
        def returnWerkvoorbereidersAanemers():
            werkvoorbereiders = []
            for projectleider in klantMedewerkersqs.iterator():
                if projectleider.functie_medewerker == 'Werk-voorbereider':
                    result = {'id': projectleider.id,'voornaam':projectleider.name_medewerker,'achternaam':projectleider.achternaam_medewerker,'phone_no':str(projectleider.phone),'klantID': projectleider.klantID_id}
                    werkvoorbereiders.append(result)
            return werkvoorbereiders


        # Uitvorders aanermers

        def returnUitvoerdersAanermers():
            uitvoerders = []
            for uitvoerder in klantMedewerkersqs.iterator():
                if uitvoerder.functie_medewerker == 'Uitvoerder':
                    result = {'id': uitvoerder.id,'voornaam':uitvoerder.name_medewerker,'achternaam':uitvoerder.achternaam_medewerker,'phone_no':str(uitvoerder.phone),'klantID': uitvoerder.klantID_id}
                    uitvoerders.append(result)
            return uitvoerders
        
        
        # project nummer get the 2 first cijfers from year
        current_year = str(date.today().year)
        twocijfers_from_year = current_year[2:]
        projectnr_ = twocijfers_from_year + projectnr
        # status = serializers.serialize('json', statusqs) # status query set

       

        # vertegenwoordigers
        resqs = Vertegenwoordiger_Project.objects.all()
        res = serializers.serialize('json', resqs)

        # Roles uit de database
        roles = Role.objects.values_list('id','role_name')

        functies = Functie.objects.values_list('id','functie','rol_id')
        # roleSerializer = serializers.serialize('json', roles)
        

        # countries cities
        nederland = 'Nederland'
        country_nederland= CountryInfo(nederland)
        provincies_Nederland = country_nederland.provinces()
        england = 'Uk'
        country_england = CountryInfo(england)
        provincies_England = country_england.provinces()
        provincies = {
            'nl':provincies_Nederland,
            'en': provincies_England
        }
        context = {
            'projectnr': projectnr_,
            # 'status': status,
            'klant': klant.data,
            'projectleiders': self.getMedewerkersperFunctie('Projectleider'),
            'projectleidersAanemers': returnProjectleidersAanemers(),
            'werkvoorbereiders': self.getMedewerkersperFunctie('Werkvoor-bereider'),
            'werkvoorbereidersAanemers':returnWerkvoorbereidersAanemers(),
            'uitvoerders':returnUitvoerdersAanermers(),
            'vertegenwoordigers': res,
            'medewerkers': medewerkers.data,
            'provincies': provincies,
            'roles': roles,
            'functies': functies,
        }
        return Response({
            'success': 'success loading project context',
            'context': context
            })