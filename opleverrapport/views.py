from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Opleverrapport
from project.models import Project
from users.models import MedewerkerProfile
from mpo.models import Site,Icem
import datetime
# Create your views here.

class GetOpleverrapportOverzicht(APIView):
     # GET ICEM GEGEVENS
    def getICemData(self,icemID):
        try:
            icem = Icem.objects.filter(id=icemID).get()
            if icem.energieModule is None or icem.icemType is None or icem.positieIcem is None:
                return "Geen"
            
            return self.checkIfValueIsNone(icem.energieModule) + self.checkIfValueIsNone(icem.icemType) + ' ' + self.checkIfValueIsNone(icem.positieIcem)
        except Exception as e:
            return str(e)

    # TEST RAPPORT EXIST ?
    def checkIftestRapportExist(self,siteID,idProject):
        try:
            if Opleverrapport.objects.filter(site_id = siteID,project_id=idProject).exists():
                return 'Ja'
            else:
                return 'Nee'
        except Exception as e:
            return str(e)

    # GET DATUM AANGEMAAKT
    def getDatumTestrapport(self,siteID,idProject):
        datum = ''
        try:
            if Opleverrapport.objects.filter(site_id = siteID,project_id=idProject).exists():
                testrapport = Opleverrapport.objects.filter(site_id = siteID,project_id=idProject).get()
                datum = testrapport.last_edit_datum
                return datum
            else:
                datum = 'N.V.T'
                return datum
        except Exception as e:
            return str(e)
    def getDefinitiefTestrapport(self,siteID,idProject):
        isdefiniet = ''
        if Opleverrapport.objects.filter(site_id = siteID,project_id=idProject).exists():
            testrapport = Opleverrapport.objects.filter(site_id = siteID,project_id=idProject).get()
            
            if testrapport.opleverrapport_definitief == 1 :
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
        for site in Site.objects.filter(projectId_id = idProject):
            context.append({
                'blok': self.checkIfValueIsNone(site.blok),
                'bouwnr': self.checkIfValueIsNone(site.bouwnr),
                'straat': self.checkIfValueIsNone(site.straat) + ' ' + self.checkIfValueIsNone(site.huisnr),
                'postcode': self.checkIfValueIsNone(site.postcode),
                'icem': self.getICemData(site.icemId_id),
                'opleverrapportaangemaakt': self.checkIftestRapportExist(site.id,idProject),
                'datumrapportrapportAangemaakt': self.getDatumTestrapport(site.id,idProject),
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

class GetOpleverrapport(APIView):
    def getAuthorName(self,id):
        author = MedewerkerProfile.objects.filter(id=id).get()
        name  = author.achternaam + ' ' + author.voornaam
        return name
    def post(self,request,format=None):
        data = self.request.data
        if Opleverrapport.objects.filter(project_id = data['project_id'],site_id= data['site_id']).exists():

            opleverapport = Opleverrapport.objects.filter(project_id = data['project_id'],site_id= data['site_id']).get()
            
            context = {
                'id': opleverapport.id,
                'last_edit_datum': opleverapport.last_edit_datum,
                'author_id':  self.getAuthorName(opleverapport.author_id),
                'druktest': opleverapport.druktest,
                'vacumeren': opleverapport.vacumeren,
                'datatest_npi_tool': opleverapport.datatest_npi_tool,
                'pragrammeren_warmtepomp': opleverapport.pragrammeren_warmtepomp,
                'testHomecontroller': opleverapport.testHomecontroller,
                'doorvoeren_afgedicht': opleverapport.doorvoeren_afgedicht,
                'leiding_afgedopt': opleverapport.leiding_afgedopt,
                'reinigen_module': opleverapport.reinigen_module,
                'visuele_inspectie_binnenzijde': opleverapport.visuele_inspectie_binnenzijde,
                'visuele_inspectie_buitenzijde': opleverapport.visuele_inspectie_buitenzijde,
                'bouwrouting_op_unit': opleverapport.bouwrouting_op_unit,
                'transportklarr_gemaakt': opleverapport.transportklarr_gemaakt,
                'router': opleverapport.router,
                'poe24v': opleverapport.poe24v,
                'poe48v': opleverapport.poe48v,
                'din_rail': opleverapport.din_rail,
                'utp_kabel_groen': opleverapport.utp_kabel_groen,
                'utp_kabel_blauw': opleverapport.utp_kabel_blauw,
                'utp_kabel_grijs': opleverapport.utp_kabel_grijs,
                'utp_kabel_zwart': opleverapport.utp_kabel_zwart,
                'boilersensor': opleverapport.boilersensor,
                'th1_kabel_display_kabel': opleverapport.th1_kabel_display_kabel,
                'homeController_set': opleverapport.homeController_set,
                'omvormer': opleverapport.omvormer,
                'sem_kast': opleverapport.sem_kast,
                'kwh_meter': opleverapport.kwh_meter,
                'p5stekker_omvormer': opleverapport.p5stekker_omvormer,
                'kampstrup_meter_21': opleverapport.kampstrup_meter_21,
                'landis_gyr_meter': opleverapport.landis_gyr_meter,
                'wtw': opleverapport.wtw,
                'soft_encloser': opleverapport.soft_encloser,
                'tongdy': opleverapport.tongdy,
                'procon': opleverapport.procon,
                'antenne': opleverapport.antenne,
                'afvoer_flexbuis_slang': opleverapport.afvoer_flexbuis_slang,
                'sifon': opleverapport.sifon,
                'rode_sensor': opleverapport.rode_sensor,
                'grijs_zwart_sensor': opleverapport.grijs_zwart_sensor,
                'aansluitslang_zwart': opleverapport.aansluitslang_zwart,
                'lange_schroeven': opleverapport.lange_schroeven,
                'vilblokjes_oranje': opleverapport.vilblokjes_oranje,
                'flow_sensor': opleverapport.flow_sensor,
                'doorlock': opleverapport.doorlock,
                'plexiplaat_e_module': opleverapport.plexiplaat_e_module,
                'wielen': opleverapport.wielen,
                'opleverrapport_definitief': opleverapport.opleverrapport_definitief,
                'opleverrapport_definitief_datum': opleverapport.opleverrapport_definitief_datum,
                
            }
            return Response({'context': context})
        else:
            return Response({'context': None})

class CreateOpleverRapport(APIView):
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

    def createOpleverRapport(self,projectId,siteId,data):
            if Opleverrapport.objects.filter(site_id = siteId,project_id = projectId).exists():
                try:
                    try :
                    
                        opleverrapport = Opleverrapport.objects.filter(site_id = siteId,project_id = projectId).update( **data) 

                    except Exception as e:
                        return ({'error':str(e)})
                    return ({'success':'bewerkt'})
                except Exception as e:
                    return ({'error': str(e)})
            
            else:
                try:
                    try:
                        opleverrapport = Opleverrapport.objects.create(**data)
                        opleverrapport.save()
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
    def checkTrueFalseString(self,args):
        if args == True:
            args = "1"
    def post(self,request,format=None):
        data = self.request.data
        self.user= int(data['author_id'])
        project = self.getprojectId(data['project_id'])
        siteId = data['site_id']
        # data['']
        print(data)
        
        # Check if one of the oranje Fields are ja
        # if data['sn_label_op_frame'] ==True:
        #     data['sn_label_op_frame'] = "1"
        # if data['wtw_debieten_control'] == True:
        #     data['wtw_debieten_control'] = "1"
        # if data['transportlabel_uitgevoerd'] == True:
        #     data['transportlabel_uitgevoerd'] = "1"
        # if data['eindschoonmaak_uitgevoerd'] == True:
        #     data['eindschoonmaak_uitgevoerd'] = "1"
        # if data['transport_gereed'] == True:
        #     data['transport_gereed'] = "1"
        # if data['eindcontrole'] == True:
        #     data['eindcontrole'] = "1"

        if data['druktest'] != "1" or data['vacumeren'] != "1"  or  data['datatest_npi_tool'] != "1"  or data['pragrammeren_warmtepomp'] != "1" or data['testHomecontroller'] != "1" or data['doorvoeren_afgedicht'] != "1" or data['leiding_afgedopt'] != "1" or data['reinigen_module'] != "1" or data['visuele_inspectie_binnenzijde'] != "1" or data['visuele_inspectie_buitenzijde'] != "1" or data['bouwrouting_op_unit'] != "1" or data['transportklarr_gemaakt'] != "1":
            data['opleverrapport_definitief'] = 0
            data['opleverrapport_definitief_datum'] = ''
        else:
            
            data['opleverrapport_definitief'] = 1
            data['opleverrapport_definitief_datum'] = self.getToday()
        
        try: 
            response = self.createOpleverRapport(project,siteId,data)
            if response['success'] == 'aangemaakt':
                return Response({'success': 'Testrapport met success aangemaakt'})
            elif response['success'] == 'bewerkt':
                return Response({'success': 'Testrapport met success bijgewerkt'})
            else:
                return Response({'error': response['error']})

        except Exception as e:
            return Response({'error': str(e)})