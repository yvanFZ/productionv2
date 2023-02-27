import json
from multiprocessing import context
from rest_framework.views import APIView
from rest_framework.response import Response
import datetime
from datetime import date
from django.core import serializers
from countryinfo import CountryInfo
from .serializer import ProjectIcemSerializer,ProjectSerializer,KlantSerializer,KlantMedewerkerSerializer
from .models import Project,ProjectIcem,Vertegenwoordiger_Project,KlantMedewerker,Klant
from mpo.models import Site,Icem
from users.models import MedewerkerProfile,klantWoningbouw
from users.serializers import MedewerkerSerializer,klantWoningbouwSerializer

# GET DATEFORMAT
def getDateformat(dateString):
     
    if dateString !="":
        format_str = '%d-%m-%Y' # The format
        formatstringDate = datetime.datetime.strptime(dateString, format_str)
        # formatstringDate_ = formatstringDate.strftime('%d-%m-%Y')
        return formatstringDate
    else:
        return None
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

# UPDATE PROJECT
class UpdateProject(APIView):
    def getMedewerkerId(self,id):
        project = Project.objects.filter(id=id).get()
        return project.klant_id
    def post(self,request,format=None):
        data = self.request.data
        #Get medewerkerId from the projecttable
        medewerkerId = self.getMedewerkerId(data['id'])
        try:
            Klant.objects.filter(id=medewerkerId).update(klantnaam=data['klantnaam'])
            Project.objects.filter(id=data['id']).update(
                renovatie_nieuwbouw=data['renovatie_nieuwbouw'],projectStatus=data['projectstatus'],
                projectnaam=data['projectnaam'],plaats=data['plaats'],
                provincie=data['provincie'],land=data['land'],
                datumSystemInvoer=data['datum_systeem_invoer'],startDatum=data['startdatum'],
                offertedatum=data['offertedatum'],
                )
            return Response({'success': data['projectnaam'] + 'is successful bijgewerkt'})
        except Exception as e:
            return Response({'error': str(e)})


# GET ALL PROJECTS
class AllProjectsList(APIView):
    def get(self,request,format=None):
        try:

            projects = Project.objects.filter('projectnr').get()
            print(projects)
          
            projects_serialiser = serializers.serialize('json', projects)
            # projects_serialiser = json.dumps(projects), content_type='application/json'
            return Response({
            'data': projects_serialiser,
        })
        except Exception as e:

            return Response({
                'error': str(e)
            })

# GET ALL PROJECTVIEW

class GetAllProjects(APIView):
    klantnameObject = getKlantNaam
    landObject = getLandNaam
    dateformat = getDateformat

    def getIcemType(self,projectID):
        icemTypes = []
        
        for site in Site.objects.filter(projectId_id=projectID):
            icemType = Icem.objects.filter(id=site.icemId_id).get() 
            icemTypes.append(icemType.icemType)
        return icemTypes
    def checkIfIcemTypeexist(self,icemData,typeIcem):
        icemTypeArray = []
        if typeIcem in icemData:
            icemTypeArray.append(typeIcem)
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
                'datum_systeem_invoer': getDateformat(project.datumSystemInvoer),
                'startdatum': getDateformat(project.startDatum),
                'offertedatum': getDateformat(project.offertedatum)
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


# CREATE MEDEWERKER KLANT VIEW
class CreateKlantMedewerkerView(APIView):
    def post(self, request, format=None):
        data = self.request.data
        nameMedewerker = data['nameMedewerker']
        achternaamMedewerker = data['achternaamMedewerker']
        telefoonMedewerker = data['telefoonMedewerker']
        functieMedewerker = data['functieMedewerker']
        klantId = data['klantId']
        
        # KLANT ID
        klant = Klant.objects.filter(id=klantId).get()
        
        try:
            klantMedeweker = KlantMedewerker.objects.create(name_medewerker=nameMedewerker,achternaam_medewerker=achternaamMedewerker,phone=telefoonMedewerker,functie_medewerker=functieMedewerker,klantID_id=klant.id)
            klantMedeweker.save()
            return Response({'success': nameMedewerker + 'is successful aangemaakt'})
        except Exception as e:
            return Response({'error': str(e)})

class GetProjectById(APIView):

    project_class = ProjectSerializer
    klantnameObject = getKlantNaam
    # GET ALL PROJECT OBJECT
    def get_queryset(self):
        projects = Project.objects.all()
        return projects

   
    
    # GET WERKVOORBEREIDER Aanemer
    def getWerkVoorbereiderAanemer(self,id):
        if id !=0:
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
        if id !=0:
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
        if id !=0:
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
        if id != 0:
            werkvoorbereiderFZ = MedewerkerProfile.objects.filter(id=id).get()
            werkvoorbereiderFZserializer = {
                'name':werkvoorbereiderFZ.voornaam + ' '+werkvoorbereiderFZ.achternaam,
                'phone': str(werkvoorbereiderFZ.phone_no)
            }
            return werkvoorbereiderFZserializer 
        else:
            return None
    
     # GET PROJECTLEIDER FZ
    def getProjectleiderFZ(self,id):
        if id != 0:
            projectleiderFZ = MedewerkerProfile.objects.filter(id=id).get()
            projectleiderFZserializer = {
                'name':projectleiderFZ.voornaam + '  '+ projectleiderFZ.achternaam,
                'phone': str(projectleiderFZ.phone_no)
            }
            return projectleiderFZserializer
        else:
            return None

    

    def post(self,request, *args,**kwargs):
        data = self.request.data
        # id = data['id']
        data_projects = self.get_queryset()

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
        
        for project in data_projects:
            if int(data) == project.id:
                projectnummer = project.projectnr
                klantnaam = self.klantnameObject(project.klant_id)
                projectnaam = project.projectnaam
                plaats = project.plaats
                provincie = project.provincie
                projectstatus = project.projectStatus
                werkVoorbereiderAanemer = self.getWerkVoorbereiderAanemer(project.selectedWerkvoorbereiderAanmelder)
                projectleiderAanemer = self.getProjectleiderAanemer(project.selectedProjectleiderAanmelder)
                uitvoerderAanemer = self.getUitvoerderAanemer(project.selectedUitvoerderAanmelder)
                werkVoorbereiderFZ = self.getWerkvoorbereiderFZ(project.selectedWerkvoorbereiderFz)
                projectleiderFZ = self.getProjectleiderFZ(project.selectedProjecleiderFz)
  
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

        }
        return Response({'dataprojectbyID': context})



class CreateProjectView(APIView):
    def post(self, request, format=None):
        if(self.request.data):
            data = self.request.data
            projectnr = data['projectnr']
            renovatie_nieuwbouw = data['renovatie_nieuwbouw_']
            projectStatus = data['projectStatus']
            projectnaam = data['projectnaam']
            plaats = data['plaats']
            provincie = data['provincie']
            land = data['land']
            klant_id = data['selectedKlanten']
            offertenr = data['offertenr']
            exactnr = data['exactnr']
            debiteurnr = data['debiteurnr']
            inopdrachtvoor_ventilatieinstallatie = data['inopdrachtvoor_ventilatieinstallatie']
            onderaannemers_ventilatieinstallatie = data['onderaannemers_ventilatieinstallatie']
            ordernr_onderaannemer_ventilatieinstallatie = data['ordernr_onderaannemer_ventilatieinstallatie']
            inopdrachtvoor_vloerverwarming = data['inopdrachtvoor_vloerverwarming']
            onderaannemers_vloerverwarming = data['onderaannemers_vloerverwarming']
            ordernr_onderaannemer_vloerverwarming = data['ordernr_onderaannemer_vloerverwarming']
            inopdrachtvoor_zonnepanelen = data['inopdrachtvoor_']
            onderaannemers_zonnepanelen = data['onderaannemers_']
            ordernr_onderaannemer_zonnepanelen = data['ordernr_onderaannemer']
            datumSystemInvoer = data['system_datum_invoer']
            startDatum = data['startDatum']
            offertedatum=data['offerteDatum']
            uitlijkDatumOpdrachtIndienWTW = data['uitlijk_datum_opdracht_indien_wtw']
            uitlijkDatumOpdrachtAlleenICEM = data['uitlijk_datum_opdracht_alleen_icem']
            opmerking = data['opmerking']
            selectedProjectleiderFz = data['selectedProjecleiderFz']
            selectedProjectleiderAanmelder = data['selectedProjecleider']
            selectedUitvoerderAanmelder = data['selectedUivoerder']
            selectedWerkvoorbereiderAanmelder = data['selectedwerkvoorbereider']
            selectedWerkvoorbereiderFz = data['selectedWerkvoorbereiderFz']


            if selectedWerkvoorbereiderFz == '':
                selectedWerkvoorbereiderFz  = None
            else:
                    selectedWerkvoorbereiderFz = selectedWerkvoorbereiderFz

            if onderaannemers_ventilatieinstallatie == '':
                onderaannemers_ventilatieinstallatie = None
            else:
                onderaannemers_ventilatieinstallatie = onderaannemers_ventilatieinstallatie

            if onderaannemers_vloerverwarming == '':
                onderaannemers_vloerverwarming = None
            else:
                onderaannemers_vloerverwarming = onderaannemers_vloerverwarming
            
            if onderaannemers_zonnepanelen == '':
                onderaannemers_zonnepanelen = None
            else: 
                onderaannemers_zonnepanelen = onderaannemers_zonnepanelen
            
            try:
                if projectnr != None:
                    project =  Project.objects.create(projectnr=projectnr,renovatie_nieuwbouw = renovatie_nieuwbouw,projectStatus=projectStatus,
                        plaats=plaats,provincie=provincie,land=land,klant_id=klant_id,offertenr=offertenr,exactnr=exactnr,debiteurnr=debiteurnr,
                        projectnaam=projectnaam,inopdrachtvoor_ventilatieinstallatie=inopdrachtvoor_ventilatieinstallatie,
                        onderaannemers_ventilatieinstallatie=onderaannemers_ventilatieinstallatie,ordernr_onderaannemer_ventilatieinstallatie=ordernr_onderaannemer_ventilatieinstallatie,
                        inopdrachtvoor_vloerverwarming=inopdrachtvoor_vloerverwarming,onderaannemers_vloerverwarming=onderaannemers_vloerverwarming,
                        ordernr_onderaannemer_vloerverwarming=ordernr_onderaannemer_vloerverwarming,inopdrachtvoor_zonnepanelen=inopdrachtvoor_zonnepanelen,
                        onderaannemers_zonnepanelen=onderaannemers_zonnepanelen,ordernr_onderaannemer_zonnepanelen=ordernr_onderaannemer_zonnepanelen,
                        datumSystemInvoer=datumSystemInvoer,startDatum=startDatum,offertedatum=offertedatum,uitlijkDatumOpdrachtIndienWTW=uitlijkDatumOpdrachtIndienWTW,
                        uitlijkDatumOpdrachtAlleenICEM=uitlijkDatumOpdrachtAlleenICEM,opmerking=opmerking,selectedProjecleiderFz=selectedProjectleiderFz,selectedProjectleiderAanmelder=selectedProjectleiderAanmelder,
                        selectedUitvoerderAanmelder = selectedUitvoerderAanmelder,selectedWerkvoorbereiderAanmelder=selectedWerkvoorbereiderAanmelder,selectedWerkvoorbereiderFz=selectedWerkvoorbereiderFz
                        )
                    project.save()
                    return Response({'success': 'Project met success aangemaakt'})
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

    def get(self, request, format=None):
        # medewerkers
        medewerkersqs = MedewerkerProfile.objects.all()
        medewerkers = MedewerkerSerializer(medewerkersqs,many=True)

        # klant medewerkers
        klantMedewerkersqs = KlantMedewerker.objects.all()
        klantMedewerkers = KlantMedewerkerSerializer(klantMedewerkersqs,many=True)

        # klanten
        klantqs = Klant.objects.all()
        klant = KlantSerializer(klantqs,many=True)


        projectnr = self.projectnr()
        
        # Projecleiders fz
        def returnProjectleiders():
            projectleiders = []
            for projectleider in medewerkersqs.iterator():
                if projectleider.functie_id == 2:
                    result = {'id': projectleider.id,'voornaam':projectleider.voornaam,'achternaam':projectleider.achternaam,'phone_no':str(projectleider.phone_no)}
                    projectleiders.append(result)
            return projectleiders
        
        # ProjectLeiders aanemers
        def returnProjectleidersAanemers():
            projectleiders = []
            for projectleider in klantMedewerkersqs.iterator():
                if projectleider.functie_medewerker == "Projectleider":
                    result = {'id': projectleider.id,'voornaam':projectleider.name_medewerker,'achternaam':projectleider.achternaam_medewerker,'phone_no':str(projectleider.phone)}
                    projectleiders.append(result)
            return projectleiders
        
        # Voorberediers FZ
        def returnWerkvoorbereiders():
            werkvoorbereiders = []
            for projectleider in medewerkersqs.iterator():
                if projectleider.functie_id ==3:
                    result = {'id': projectleider.id,'voornaam':projectleider.voornaam,'achternaam':projectleider.achternaam,'phone_no':str(projectleider.phone_no)}
                    werkvoorbereiders.append(result)
            return werkvoorbereiders

        # Voorberediers aanemers
        def returnWerkvoorbereidersAanemers():
            werkvoorbereiders = []
            for projectleider in klantMedewerkersqs.iterator():
                if projectleider.functie_medewerker == 'Werkvoorbereider':
                    result = {'id': projectleider.id,'voornaam':projectleider.name_medewerker,'achternaam':projectleider.achternaam_medewerker,'phone_no':str(projectleider.phone)}
                    werkvoorbereiders.append(result)
            return werkvoorbereiders


        # Uitvorders aanermers

        def returnUitvoerdersAanermers():
            uitvoerders = []
            for uitvoerder in klantMedewerkersqs.iterator():
                if uitvoerder.functie_medewerker == 'Uitvoerder':
                    result = {'id': uitvoerder.id,'voornaam':uitvoerder.name_medewerker,'achternaam':uitvoerder.achternaam_medewerker,'phone_no':str(uitvoerder.phone)}
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
            'projectleiders': returnProjectleiders(),
            'projectleidersAanemers': returnProjectleidersAanemers(),
            'werkvoorbereiders': returnWerkvoorbereiders(),
            'werkvoorbereidersAanemers':returnWerkvoorbereidersAanemers(),
            'uitvoerders':returnUitvoerdersAanermers(),
            'vertegenwoordigers': res,
            'medewerkers': medewerkers.data,
            'provincies': provincies
        }
        return Response({
            'success': 'success loading project context',
            'context': context
            })