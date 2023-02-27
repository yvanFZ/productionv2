from rest_framework.views import APIView
# Create your views here.
from mpo.models import Site,Icem,Planning,ProductiebonStatus
from opleverrapport.models import Opleverrapport
from testrapport.models import Testrapport
from rest_framework.response import Response
from project.models import Project
from mpo.models import ProductiebonStatus
from datetime import date



class GetProductiestatusIcemOverzicht(APIView):
    # icem gegevens + berekeningen

    def getIcemType(self,id):
        icemType = Icem.objects.filter(id=id).get()
        return icemType.icemType
    
    def checkifsitehasmissingondedelen(self,siteID, projectID):
        
        # check if opleverrapport exist
        if Opleverrapport.objects.filter(site_id=siteID,project_id=projectID).exists():
            
            opleverrapport = Opleverrapport.objects.filter(site_id=siteID,project_id=projectID).get()
            object = {
                'router': opleverrapport.router,
                'poe24v' : opleverrapport.poe24v,
                'poe48v' : opleverrapport.poe48v,
                'din_rail' : opleverrapport.din_rail,
                'utp_kabel_groen' : opleverrapport.utp_kabel_groen,
                'utp_kabel_blauw' : opleverrapport.utp_kabel_blauw,
                'utp_kabel_zwart' : opleverrapport.utp_kabel_zwart,
                'boilersensor' : opleverrapport.boilersensor,
                'th1_kabel_display_kabel' : opleverrapport.th1_kabel_display_kabel,
                'homeController_set' : opleverrapport.homeController_set,
                'omvormer' : opleverrapport.omvormer,
                'sem_kast' : opleverrapport.sem_kast,
                'kwh_meter' : opleverrapport.kwh_meter,
                'p5stekker_omvormer' : opleverrapport.p5stekker_omvormer,
                'kampstrup_meter_21' : opleverrapport.kampstrup_meter_21,
                'landis_gyr_meter' : opleverrapport.landis_gyr_meter,
                'wtw' : opleverrapport.wtw,
                'soft_encloser' : opleverrapport.soft_encloser,
                'tongdy' : opleverrapport.tongdy,
                'procon' : opleverrapport.procon,
                'antenne' : opleverrapport.antenne,
                'afvoer_flexbuis_slang' : opleverrapport.afvoer_flexbuis_slang,
                'sifon' : opleverrapport.sifon,
                'rode_sensor' : opleverrapport.rode_sensor,
                'grijs_zwart_sensor' :opleverrapport.grijs_zwart_sensor,
                'aansluitslang_zwart' : opleverrapport.aansluitslang_zwart,
                'lange_schroeven' : opleverrapport.lange_schroeven,
                'vilblokjes_oranje' : opleverrapport.vilblokjes_oranje,
                'flow_sensor' : opleverrapport.flow_sensor,
                'doorlock' : opleverrapport.doorlock,
                'plexiplaat_e_module' : opleverrapport.plexiplaat_e_module,
                'wielen' : opleverrapport.wielen
           
            }
            
            # missendeOnderdelen = [router,poe24v,poe48v,din_rail,utp_kabel_groen,utp_kabel_blauw,utp_kabel_zwart,boilersensor,
            #     th1_kabel_display_kabel,homeController_set,omvormer,sem_kast,kwh_meter,p5stekker_omvormer,kampstrup_meter_21,
            #     landis_gyr_meter,wtw,soft_encloser,tongdy,procon,antenne,afvoer_flexbuis_slang,sifon,rode_sensor,grijs_zwart_sensor,
            #     aansluitslang_zwart,lange_schroeven,vilblokjes_oranje,flow_sensor,doorlock,plexiplaat_e_module,wielen]

            # check in de array if there is string missende
            return object
        
        else:
            return []
    
    def checkifInSiteBoolean(self,args):
        
        if  type(args) is dict:
            y = []
            x = args.values()
            # print(list(x))
            y = list(x)
            if y.__contains__(False):
                    return False
            else:
                    return True 
        else:
            return False
    def checkiftransportgereedBijdezeSite(self,siteID, projectID):
        if Testrapport.objects.filter(site_id=siteID,project_id=projectID).exists():
             testrapport = Testrapport.objects.filter(site_id=siteID,project_id=projectID).get()
             is_transportgereed = testrapport.transport_gereed
             if is_transportgereed == 1:
                 return True
             else:
                 return False
        else:
            return False
    def checkiftestrapportdefinietBijdezeSite(self,siteID, projectID):
        if Testrapport.objects.filter(site_id=siteID,project_id=projectID).exists():
             testrapport = Testrapport.objects.filter(site_id=siteID,project_id=projectID).get()
             is_transportgereed = testrapport.testrapport_definitief
             if is_transportgereed == 1:
                 return True
             else:
                 return False
        else:
            return False
    def getObjectMissendeOndelen(self,siteID, projectID):
        missendeondedelenArray = self.checkifsitehasmissingondedelen(siteID,projectID)
        # missendeondedelenObject = {
        #     'router': missendeondedelenArray[0],
        #     'poe24v': 
        # }
        return  missendeondedelenArray
    def getProjectNaam(self,projectID):
        try:
            if Project.objects.filter(id=projectID).exists():
                project = Project.objects.filter(id=projectID).get()
                return project.projectnr
            else:
                return None
        except Exception as e:
            return Response({'error':str(e)})
    def leverDatumModule(self,icemId):
        icem = Icem.objects.filter(id=icemId).get()
        planningId = icem.planningId_id
        planning = Planning.objects.filter(id=planningId).get()
        return planning.leverdatum
        
    def getGridData(self,siteID, projectID):
        # get site gegevens
        arrayMissendeObjects =  self.getObjectMissendeOndelen(siteID,projectID)

        site = Site.objects.filter(id=siteID,projectId_id=projectID).get()
        projectId = Project.objects.filter(id=projectID).get()
        # check if its exist
        transportgereed = None
        testrapport_definitief = None
        if Testrapport.objects.filter(site_id=siteID,project_id=projectID).exists():
            testrapport = Testrapport.objects.filter(site_id=siteID,project_id=projectID).get()
            transportgereed = testrapport.transport_gereed
            testrapport_definitief = testrapport.testrapport_definitief
        else:

            transportgereed = None
            testrapport_definitief = None
        productiegereed = None
        if ProductiebonStatus.objects.filter(site_id=siteID,projectId_id = projectID).exists():
            productiebonstatus = ProductiebonStatus.objects.filter(site_id=siteID,projectId_id = projectID).get()
            productiegereed = productiebonstatus.productiegereed
            productiegereed_datum = productiebonstatus.productieDatum
        else:
            productiegereed = None
            productiegereed_datum = None


        object = {
            'projectnummer': self.getProjectNaam(projectId.id),
            'bouwnr': site.bouwnr,
            'straat': site.straat,
            'huisnr': site.huisnr,
            'postcode': site.postcode,
            'missende_onderdelen': arrayMissendeObjects,
            'transportgereed': transportgereed,
            'testrapport_definitief': testrapport_definitief,
            'leverdatum': self.leverDatumModule(site.icemId_id),
            'productiegereed': productiegereed,
            'productiegereed_datum': productiegereed_datum
        }
        return object

    def post(self,request,format=None):
        data = self.request.data
        icemType = []
        is_missendeOnderdelenBijdezeSite = []
        transportgereed = []
        testrapportdefinitief = []
        leverdatumModule = []
        datagridData = []
        try:

            for site in Site.objects.filter(projectId_id=(data)):
                # get the icem type
                icemType_ = self.getIcemType(site.icemId_id) 
                is_missendeOnderdelenBijdezeSite_ = self.checkifInSiteBoolean(self.checkifsitehasmissingondedelen(site.id,data))
                is_getransportgereed = self.checkiftransportgereedBijdezeSite(site.id,data)
                testrapportdefinitief_ = self.checkiftestrapportdefinietBijdezeSite(site.id,data)
                leverdatumModule_ = self.leverDatumModule(site.icemId_id)
                datagridData_ = self.getGridData(site.id,data)

                icemType.append(icemType_)
                is_missendeOnderdelenBijdezeSite.append(is_missendeOnderdelenBijdezeSite_)
                transportgereed.append(is_getransportgereed)
                testrapportdefinitief.append(testrapportdefinitief_)
                leverdatumModule.append(leverdatumModule_)
                datagridData.append(datagridData_)

            jsonresponse = {
                'icemType': icemType,
                'missendeOnderdelen': is_missendeOnderdelenBijdezeSite,
                'transportgereed': transportgereed,
                'testrapportdefinitief': testrapportdefinitief,
                'datagrid': datagridData

            }
            return Response({'data': jsonresponse})
        except Exception as e:
            print(e)
            return Response({'error': str(e)})

class AanmakenProductieStatusIcem(APIView):
    def getDatetoday(self):
        today = date.today()
        d = today.strftime("%d-%m-%Y")
        return d

    def aanmakenProductieStatusIcem(self,args):
        site = Site.objects.filter(bouwnr=args['site_id'],projectId_id = args['projectId_id']).get()
        print(site)
        # if Project.objects.filter()
        if ProductiebonStatus.objects.filter(projectId_id = args['projectId_id'],site_id = site.id).exists():
            # Update the row
            try:
                productie_datum = self.getDatetoday()
                ProductiebonStatus.objects.filter(projectId_id = args['projectId_id'],site_id = site.id).update(
                    productiegereed=args['productiegereed'],productieDatum=productie_datum
                )
                return 'success bijgewerkt'
            except Exception as e:
                return  str(e)
        else:
            try:
                args['productieDatum'] = self.getDatetoday()
                print(args)
                ProductiebonStatus.objects.create(**args)
                return 'success aangemaakt'
            except Exception as e:
                return str(e)


    def post(self,request,format=None):
        data = self.request.data
        print(data)
        try:
            message = self.aanmakenProductieStatusIcem(data)
            print(message)
            return Response({'success': message})
        except Exception as e:
            return Response({'error': str(e)})
             