from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Testrapport
from project.models import Project
from users.models import MedewerkerProfile
from mpo.models import Site,Icem
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
import datetime
# Create your views here.

def get_project_object(id):
    try:
        project = Project.objects.filter(id=id).get()
        return project
    except Exception as e:
        return str(e)
def get_site_object(id):
    try:
        site = Site.objects.get(id = id)
        return site
    except Exception as e:
        return str(e)

class GetTestrapport(APIView):
    
    def getAuthorName(self,id):
        author = MedewerkerProfile.objects.filter(id=id).get()
        name  = author.achternaam + ' ' + author.voornaam
        return name
    def post(self,request,format=None):
        data = self.request.data
        site = get_site_object(data['site_id'])
        project = get_project_object(data['project_id'])
        if Testrapport.objects.filter(project = project,site=site).exists():
            testrapport = Testrapport.objects.filter(project=project,site=site).get()
            print(testrapport)
            context = {
                'id': testrapport.id,
                'last_edit_datum': testrapport.last_edit_datum,
                'author_id':  self.getAuthorName(testrapport.author_id),
                'druktest': testrapport.druktest,
                'druktest_datum': testrapport.druktest_datum,
                'luchtest': testrapport.luchtest,
                'luchtest_datum': testrapport.luchtest_datum,
                'druk_cv': testrapport.druk_cv,
                'flow_cv': testrapport.flow_cv,
                'standtijd_cv': testrapport.standtijd_cv,
                'druktap': testrapport.druktap,
                'standtijd_druktap': testrapport.standtijd_druktap,
                'npidatatestuitgevoerd': testrapport.npidatatestuitgevoerd,
                'npidatatesuitgevoerd_datum': testrapport.npidatatesuitgevoerd_datum,
                'programmeerSD_kaart': testrapport.programmeerSD_kaart,
                'aanvoertemp': testrapport.aanvoertemp,
                'tijd_legionella': testrapport.tijd_legionella,
                'frame': testrapport.frame,
                'sem_gateway': testrapport.sem_gateway,
                'sem_mac_adres': testrapport.sem_mac_adres,
                'warmtepomp_binnen_ftc_unit': testrapport.warmtepomp_binnen_ftc_unit,
                'warmtepomp_buiten': testrapport.warmtepomp_buiten,
                'procon': testrapport.procon,
                'ventilatie_wtw': testrapport.ventilatie_wtw,
                'kamstrup_21_rond': testrapport.kamstrup_21_rond,
                'kamstrup_403_landis_t230': testrapport.kamstrup_403_landis_t230,
                'flowmeter': testrapport.flowmeter,
                'display_mac_adres_homecontroller': testrapport.display_mac_adres_homecontroller,
                'boiler': testrapport.boiler,
                'spinvlies_voldoende': testrapport.spinvlies_voldoende,
                'bekabeling_voldoende': testrapport.bekabeling_voldoende,
                'lekvrij_door_blower_door_test': testrapport.lekvrij_door_blower_door_test,
                'spinvlies_zijkanten': testrapport.spinvlies_zijkanten,
                'eindschoonmaak_binnenzijde': testrapport.eindschoonmaak_binnenzijde,
                'stikstof_en_vacumeren_module': testrapport.stikstof_en_vacumeren_module,
                'stikstof_sterkte_bar': testrapport.stikstof_sterkte_bar,
                'stikstof_sterkte_standtijd': testrapport.stikstof_sterkte_standtijd,
                'vacumeren_module_micron': testrapport.vacumeren_module_micron,
                'vacumeren_module_standtijd': testrapport.vacumeren_module_standtijd,
                'lekdetectie': testrapport.lekdetectie,
                'lekdetectie_datum': testrapport.lekdetectie_datum,
                'sn_label_op_frame': testrapport.sn_label_op_frame,
                'wtw_debieten_control': testrapport.wtw_debieten_control,
                'transportlabel_uitgevoerd': testrapport.transportlabel_uitgevoerd,
                'eindschoonmaak_uitgevoerd': testrapport.eindschoonmaak_uitgevoerd,
                'transport_gereed': testrapport.transport_gereed,
                'transport_gereed_datum': testrapport.transport_gereed_datum,
                'eindcontrole': testrapport.eindcontrole,
                'eindcontrole_datum': testrapport.eindcontrole_datum,
                'testrapport_definitief': testrapport.testrapport_definitief,
                'testrapport_definitief_datum': testrapport.testrapport_definitief_datum,
            }
            return Response({'context': context})
        else:
            return Response({'context': None})

class CreateTestrapport(APIView):
    user = 0
    def getprojectId(self,projectId):
        project = Project.objects.filter(id=projectId).get()
        return project.id
    # def is_engineer(self):
    #     user = MedewerkerProfile.objects.filter(user_id = self.user).get()
    #     if user.functie_id == 13:
    #         return True
    #     else:
    #         return False   
    # @permission_required(is_engineer)

    def createTestRapport(self,projectId,siteId,data):
            if Testrapport.objects.filter(site_id = siteId,project_id = projectId).exists():
                try:
                    try :
                    
                        testrapport = Testrapport.objects.filter(site_id = siteId,project_id = projectId).update( **data) 

                    except Exception as e:
                        return ({'error':str(e)})
                    return ({'success':'bewerkt'})
                except Exception as e:
                    return ({'error': str(e)})
            
            else:
                try:
                    try:
                        testrapport = Testrapport.objects.create(**data)
                        testrapport.save()
                    except Exception as e:
                        print(e)
                        return ({'error':str(e)})
                    
                    return ({'success':'aangemaakt'})
                except Exception as e:
                    return ({'error': str(e)})
    
    def getToday(self):
        current_datetime = datetime.datetime.now()
        current_datetime = current_datetime.strftime('%d-%m-%Y')
        return current_datetime
    
    def post(self,request,format=None):
        data = self.request.data
        self.user= int(data['author_id'])
        project = self.getprojectId(data['project_id'])
        siteId = data['site_id']

        # Check if one of the oranje Fields are ja
        if data['sn_label_op_frame'] ==True:
            data['sn_label_op_frame'] = "1"
        if data['wtw_debieten_control'] == True:
            data['wtw_debieten_control'] = "1"
        if data['transportlabel_uitgevoerd'] == True:
            data['transportlabel_uitgevoerd'] = "1"
        if data['eindschoonmaak_uitgevoerd'] == True:
            data['eindschoonmaak_uitgevoerd'] = "1"
        if data['transport_gereed'] == True:
            data['transport_gereed'] = "1"
        if data['eindcontrole'] == True:
            data['eindcontrole'] = "1"

        if data['sn_label_op_frame'] != "1" or data['wtw_debieten_control'] != "1"  or  data['transportlabel_uitgevoerd'] != "1"  or data['eindschoonmaak_uitgevoerd'] != "1" or data['transport_gereed'] != "1" or data['eindcontrole'] != "1":
            data['testrapport_definitief'] = 0
            data['testrapport_definitief_datum'] = ''
        else:
            
            data['testrapport_definitief'] = 1
            data['testrapport_definitief_datum'] = self.getToday()
        
        try: 
            response = self.createTestRapport(project,siteId,data)
            if response['success'] == 'aangemaakt':
                return Response({'success': 'Testrapport met success aangemaakt'})
            elif response['success'] == 'bewerkt':
                return Response({'success': 'Testrapport met success bijgewerkt'})
            else:
                return Response({'error': response['error']})

        except Exception as e:
            return Response({'error': str(e)})
            
class GetTestrapportOverzicht(APIView):

      # GET ICEM GEGEVENS
    def getICemData(self,icemID):
        try:
            icem = Icem.objects.filter(site_id=icemID).get()
            if icem.energieModule is None or icem.icemType is None or icem.positieIcem is None:
                return "Geen"
            
            return self.checkIfValueIsNone(icem.energieModule) + self.checkIfValueIsNone(icem.icemType) + ' ' + self.checkIfValueIsNone(icem.positieIcem)
        except Exception as e:
            return str(e)

    # TEST RAPPORT EXIST ?
    def checkIftestRapportExist(self,siteID,idProject):
        try:
            if Testrapport.objects.filter(site_id = siteID,project_id=idProject).exists():
                return 'Ja'
            else:
                return 'Nee'
        except Exception as e:
            return str(e)

    # GET DATUM AANGEMAAKT
    def getDatumTestrapport(self,siteID,idProject):
        datum = ''
        try:
            if Testrapport.objects.filter(site_id = siteID,project_id=idProject).exists():
                testrapport = Testrapport.objects.filter(site_id = siteID,project_id=idProject).get()
                datum = testrapport.last_edit_datum
                return datum
            else:
                datum = 'N.V.T'
                return datum
        except Exception as e:
            return str(e)
    def getDefinitiefTestrapport(self,siteID,idProject):
        isdefiniet = ''
        if Testrapport.objects.filter(site_id = siteID,project_id=idProject).exists():
            testrapport = Testrapport.objects.filter(site_id = siteID,project_id=idProject).get()
            
            if testrapport.testrapport_definitief == 1 :
                isdefiniet = 'Ja'
            else:
                isdefiniet = 'Nee'

            return isdefiniet
        else:
            isdefiniet = 'N.V.T'
            return isdefiniet
      # GET MPO VOOR DE PROJECTID
    def checkIfValueIsNone(self,str):
        str_ = ''
        if str is None:
            str_ = 'Geen'
        else:
            str_ = str
        return str_ 
   
    def getMpo(self,idProject):
        context = []
        project = get_project_object(idProject)
        sites = Site.objects.filter(projectId_id = project).order_by('id')
        for site in sites:
            context.append({
                'blok': self.checkIfValueIsNone(site.blok),
                'bouwnr': self.checkIfValueIsNone(site.bouwnr),
                'straat': self.checkIfValueIsNone(site.straat) + ' ' + self.checkIfValueIsNone(site.huisnr),
                'postcode': self.checkIfValueIsNone(site.postcode),
                'icem': self.getICemData(site),
                'testrapportaangemaakt': self.checkIftestRapportExist(site.id,idProject),
                'datumtestrapportAangemaakt': self.getDatumTestrapport(site.id,idProject),
                'definitief': self.getDefinitiefTestrapport(site.id,idProject)

            })  
        return context
        
      # POST METHOD
    def post(self,request,format=None):
        data = self.request.data
        try: 
            context = self.getMpo(data['projectID'])
            return Response({'context': context})
        except Exception as e:
            return Response({'error':str(e)})

            

