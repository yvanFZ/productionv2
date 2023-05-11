
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import serializers
from project.models import Project,Klant
from .models import Site,ProductieExact,Omvormer,IcemDebiet,Semkast,Warmtepomp, WTW,Boiler,Planning,Icem,Bouwkundig,Bewoners,ProductiebonStatus
from django.db.models import Case, When
from django.db import transaction
import re


# Create your views here.
def getProject(projectid):
    try:
        project = Project.objects.filter(id=projectid).get()
        return project
    except Exception as e:
        return None
class GetAllSiteByProject(APIView):
    def getSiteArray(self,id):
    
            sites = []
            for site in Site.objects.filter(projectId_id = (id)):
                siteObject = {
                    'id': site.id,
                }
                sites.append(siteObject)
            return sites

    def post(self,request,format=None):
        data = self.request.data
   
        sites_array = self.getSiteArray(data)
        return Response({'sites': sites_array})
     
def getDigitOutString(e):
    if e != None: 
        if type(e) == str:
            x = re.findall(r'\d+', e)
            return x[0]
        else:
            return e
    
    else:
        return e
# GET MPODATA 
class GetMPO(APIView):
    def getAllmpoData(self,projectID):

        # jsonObject
        algemeneObject = []
        icemComponentenObject = []
        icemDebietObject = []
        omvormerObject = []
        planningObject = []
        bouwkundigObject = []
        productieExactObject = []
        bewonerObject = []
        jsonData = {
            'algemeene': algemeneObject,
            'icemComponenten':icemComponentenObject,
            'icemDebiet': icemDebietObject,
            'omvormer':omvormerObject,
            'planning': planningObject,
            'bouwkundig': bouwkundigObject,
            'productieExact': productieExactObject,
            'bewoner': bewonerObject

        }
        
        project = getProject(projectID)
        sites = Site.objects.filter(projectId_id = project).order_by('id')
        # siteIds = sites.values_list('id',flat=True)
        # sorted_sites = sorted(siteIds)
        # icemsTestArray = []
        
        with transaction.atomic():
            
            for site in sites:
                
                icem = Icem.objects.get(site=site)
                
                boiler = Boiler.objects.get(icem=icem)
                
                icemdebiet = IcemDebiet.objects.get(icem=icem)
                
                warmtepomp  = Warmtepomp.objects.get(icem=icem)
                
                bouwkundig = Bouwkundig.objects.get(site=site)
                omvormer = Omvormer.objects.get(icem=icem)
                bewoner = Bewoners.objects.get(site=site)
                productie = ProductieExact.objects.get(icem=icem)
                semkast = Semkast.objects.get(icem=icem)
                wtw = WTW.objects.get(icem=icem)
                planning = Planning.objects.get(icem=icem)

                print(planning)


                algemeneObject.append({
                    'bouwnr':site.bouwnr,
                    'blok': site.blok,
                    'straat': site.straat,
                    'huisnr': site.huisnr,
                    'postcode': site.postcode,
                    'bijzonderheden': site.bijzonderheden,
                    'koop_huur':site.koop_huur
                })
                icemComponentenObject.append(
                    {
                    'bouwnr':site.bouwnr,
                    'blok': site.blok,
                    'icemType': icem.icemType,
                    'energieModule': icem.energieModule,
                    'dakhelling': omvormer.dakheling,
                    'links_rechts': icem.positieIcem,
                    'aansluitingkanalen': icem.aansluitingkanalen,
                    'boilerInhoud': boiler.inhoud,
                    'merkWtw': wtw.merk,
                    'typeWtw': wtw.type,
                    'wtwDebiet': wtw.debiet,
                    'vermogenWp': warmtepomp.vermogen,
                    'kwh_meter': icem.kwh_meter,
                    'semkast': semkast.type,
                    'sensoringOptie': icem.sensoringOptie,
                    'typePrestatie': icem.type_prestatie,
                    'koeling': icem.koeling,
                    'positieWpModule': icem.positieWPmodule,

                })

                icemDebietObject.append({
                    'bouwnr':site.bouwnr,
                    'blok': site.blok,
                    'stand1': icemdebiet.stand1,
                    'stand2': icemdebiet.stand2,
                    'stand3': icemdebiet.stand3,
                    'stand4': icemdebiet.stand4,
                    'stand5': icemdebiet.stand5,

                })
                omvormerObject.append({
                    'bouwnr':site.bouwnr,
                    'blok': site.blok,
                    'omvormerOwner': omvormer.owner,
                    'omvromerMerk': omvormer.merkOmvormer,
                    'capaciteit': omvormer.capaciteit,
                    'levering_door': omvormer.levering_door,
                    'levering_datum': omvormer.levering_datum
                })
        
                planningObject.append({
                    'bouwnr':site.bouwnr,
                    'blok': site.blok,
                    'bouwnr': site.bouwnr,
                    'bouwrouting': planning.bouwrouting,
                    'leverdatum': planning.leverdatum
                })

                bouwkundigObject.append({
                    'bouwnr':site.bouwnr,
                    'blok': site.blok,
                    'nokHoogte': bouwkundig.nokHoogte,
                    'nokDiepte': bouwkundig.nokDiepte,
                    'typeDak': bouwkundig.typeDak,
                    'positiebuitendeel': bouwkundig.positieBuitendeel
                })
            
                productieExactObject.append({
                    'bouwnr':site.bouwnr,
                    'blok': site.blok,
                    'bomId': productie.bomId,
                    'exactnummer': productie.exactnummer
                })
                
                bewonerObject.append(
                            {
                            'project':project.projectnr,
                            'bouwnr': site.bouwnr,
                            'aanhef': bewoner.aanhef_bewoner,
                            'achternaam': bewoner.achternaam_bewoner,
                            'voorletter': bewoner.voorletters_bewoner,
                            'phone': bewoner.phone_bewoner,
                            'tussenvoegsel': bewoner.tussenvoegsels_bewoner,
                            'email': bewoner.email_bewoner
                            
                        }   
                        )
                
        return jsonData

    # FUNCTIE BEWONERS AANMAKEN
    def bewonerAanmaken(self,data):
        try:
            bewoner = Bewoners.objects.create(**data)
            bewoner.save()
            return bewoner
        except Exception as e:
            return str(e)
    
    def siteAanmaken(self,data):
        try:
            site = Site.objects.create(**data)
            site.save()
            return site
        except Exception as e:
            return str(e)
    def productieAanmaken(self,data):

        try:
            productie = ProductieExact.objects.create(**data)
            productie.save()
            return productie
        except Exception as e:
            return str(e)

    def omvormerAanmaken(self,data):
        try:
            omvormer = Omvormer.objects.create(**data)
            omvormer.save()
            return omvormer
        except Exception as e:
            return str(e)

    def icemdebietAanmaken(self,data):
        try:
            icemdebiet = IcemDebiet.objects.create(**data)
            icemdebiet.save()
            return icemdebiet
        except Exception as e:
            return str(e)
    
    def semkastAanmaken(self,data):
        try:
            semkast = Semkast.objects.create(**data)
            semkast.save()
            return semkast
        except Exception as e:
            return str(e)
            
    def warmtepompAanmaken(self,data):
        try:
            warmtepomp = Warmtepomp.objects.create(**data)
            warmtepomp.save()
            return warmtepomp
        except Exception as e:
            return str(e)

    def wtwAanmaken(self,data):
        try:
            wtw = WTW.objects.create(**data)
            wtw.save()
            return wtw
        except Exception as e:
            return str(e)

    def boilerAanmaken(self,data):
        try:
            boiler = Boiler.objects.create(**data)
            boiler.save()
            return boiler
        except Exception as e:
            return str(e)

    def planningAanmaken(self,data):
        try:
            planning = Planning.objects.create(**data)
            planning.save()
            return planning
        except Exception as e:
             return str(e)

    # def getprojectId(self,projectnummer):
    #     try:
    #         project = Project.objects.filter(projectnr=projectnummer).get()
    #         return project
    #     except Exception as e:
    #         return str(e)


    def IcemAanmaken(self,data): 
        try:
            icem = Icem.objects.create(**data)
            icem.save()
            return icem
        except Exception as e:
            return str(e)

    def bouwkundigAanmaken(self, data):
        try:
            bouwkundig = Bouwkundig.objects.create(**data)
            bouwkundig.save()
            return bouwkundig
        except Exception as e:
            return str(e)

    def createMPO(self,projectID):
        project =  getProject(projectID)
        if project != None:

            projectnaam =project.projectnaam
            mpo_leng = int(re.findall(r'\d+', projectnaam)[0])
            
        else:
            error = "Create project first"
            return Response({'error':error})
        # re.findall(r'\d+', projectnaam)
        
        for  i in range(mpo_leng):
           
             # create mpo tables
                bouwkundigdata = {
                    'nokHoogte': None,
                    'nokDiepte': None,
                    'typeDak': None,
                    'positieBuitendeel': None
                }
                # Planning Aanmaken
                planningdata = {
                    'bouwrouting':None,
                    'leverdatum':None,
                }
                # Boiler Aanmaken
                boilerdata = {
                    'inhoud': None
                    } 
                #   Wtw Aanmaken
                wtwdata = {
                    'merk': None,
                    'type': None,
                    'debiet': None
                }
                # Warmte pomp Aanmaken
                warmtepompdata = {
                    'vermogen': None
                    }
                # Semkast Aanmaken
                semkastdata = {
                    'type': None
                }
                # Icem debiet Aanmaken
                icemdebietdata = {
                    'stand1': None,
                    'stand2': None,
                    'stand3': None,
                    'stand4': None,
                    'stand5': None
                }
                # Productie aanmaken
                productiedata = {
                    'bomId': None,
                    'exactnummer':None,
                }
                # Omvomermer aanmaken
                omvormerdata = {
                    'merkOmvormer': None,
                    'dakheling': None,
                    'owner': None,
                    'capaciteit': None,
                    'levering_datum': None,
                    'levering_door': None,
                }
                try:
                    bouwkundigId = self.bouwkundigAanmaken(bouwkundigdata)
                   
                    planningId = self.planningAanmaken(planningdata)
                    boiler_Id = self.boilerAanmaken(boilerdata)
                    wtw_Id = self.wtwAanmaken(wtwdata)
                    warmtepompId = self.warmtepompAanmaken(warmtepompdata)
                    semkastId = self.semkastAanmaken(semkastdata)
                    icemdebietId = self.icemdebietAanmaken(icemdebietdata)
                    productieExactId = self.productieAanmaken(productiedata)
                    omvormerId = self.omvormerAanmaken(omvormerdata)
                    icemdata = {
                        'icemType' : None,
                        'energieModule' : None,
                        'positieIcem' : None,
                        'aansluitingkanalen' : None,
                        'kwh_meter' : None,
                        'koeling' : None,
                        'positieWPmodule' : None,
                        'sensoringOptie' : None,
                        'type_prestatie' : None,
                        'productieExactId': productieExactId,
                        'omvormerId': omvormerId,
                        'icemDebietId': icemdebietId,
                        'semkastId': semkastId,
                        'warmtepompId': warmtepompId,
                        'wtw_Id': wtw_Id,
                        'boiler_Id': boiler_Id,
                        'planningId': planningId
                    }
                    idIcem = self.IcemAanmaken(icemdata)
                    sitedata = {
                        'bouwnr': i+1,
                        'blok': None,
                        'straat': None,
                        'huisnr': None,
                        'postcode': None,
                        'bijzonderheden': None,
                        'koop_huur': None,
                        'bouwkundigId_id': bouwkundigId.id,
                        'icemId_id':idIcem.id,
                        'projectId_id':projectID,
                    }
                    site = self.siteAanmaken(sitedata)
                    bewonersdata = {
                    # DATA FOR BEWONERS
                    'aanhef_bewoner':None,
                    'achternaam_bewoner':None,
                    'voorletters_bewoner' : None,
                    'phone_bewoner':None,
                    'tussenvoegsels_bewoner':None,
                    'email_bewoner':None,
                    'siteId_id': site.id,
                    }
                    self.bewonerAanmaken(bewonersdata)
                
                except Exception as e:
                    return Response({'error': str(e)})

    def create_sites(self, project, mpo_len):
        all_sites = []
        for i in range(mpo_len):
            sitedata = {
            'bouwnr': 1 + i,
            'blok': None,
            'straat': None,
            'huisnr': None,
            'postcode': None,
            'bijzonderheden': None,
            'koop_huur': None,
            'projectId':project,
            }
            all_sites.append(Site(**sitedata))
        Site.objects.bulk_create(all_sites)

    def checkifProjectexist(self,id):
        if Project.objects.filter(id=id).exists():
            return True
        else:
            return False
    def post(self,request,format=None):

        projectID = self.request.data
        checkifProjectexist = self.checkifProjectexist(projectID['id'])
        
        if checkifProjectexist == True:
            
            try:
                
                if Site.objects.filter(projectId_id = projectID['id']).exists():
                    
                    data = self.getAllmpoData(projectID['id'])
                    # print(f'end Post functie {data}')
                    return Response({'data': data},status=200)
                else: 
                    try:
                        print(f'begin Post functie')
                        self.create_mpo(projectID['id'])
                        data = self.getAllmpoData(projectID['id'])
                    
                        return Response({'data': data},status=201)
                    except Exception as e:
                        
                        return Response({"error": str(e)}, status=401)
            
            except Exception as e:
                return Response({"error": str(e)}, status=401)
        else:
            return Response({'msg': 'project bestaat niet!'})
    # CREATE
    def create_icems(self, sites):
        all_icems = []
        for site in sites:
            icemdata = {
                'site': site,
                'icemType' : None,
                'energieModule' : None,
                'positieIcem' : None,
                'aansluitingkanalen' : None,
                'kwh_meter' : None,
                'koeling' : None,
                'positieWPmodule' : None,
                'sensoringOptie' : None,
                'type_prestatie' : None,
            }
            all_icems.append(Icem(**icemdata))
        Icem.objects.bulk_create(all_icems)

    # @csrf_exempt
    def delete(self, request):
        project_id = 5
        project = getProject(project_id)
        site_set = project.site_set.all()
        number_of_sites = len(site_set)
        site_set.delete()

        return Response(f"{number_of_sites} sites deleted succesfull")

    # @csrf_exempt
    def get(self, request, **kwargs): 
        projectID = 5
        project = getProject(projectID)
        if len(project.site_set.all()) == 0:
            self.create_mpo(projectID)
            status=201
        else:
            status=200
        
        data = self.getAllmpoData(projectID)
        return Response(data, status=status)

    def create_mpo(self, projectID):
        project = getProject(projectID)
        projectnaam = project.projectnaam
        # re.findall(r'\d+', projectnaam)
        mpo_leng = int(re.findall(r'\d+', projectnaam)[0])

        allBewoners = []
        allBouwkundig = []
        allPlanning = []
        allBoilers = []
        allWtw = []
        allWarmtepompen = []
        allSemkasten = []
        allIcemdebieten = []
        allProductieBon = []
        allProductieExact = []
        omvormers = []
      
        self.create_sites(project, mpo_leng)
        sites = Site.objects.filter(projectId = project).all().order_by('id')
        self.create_icems(sites)
        icems = [Icem.objects.select_related().filter(site = site).get() for site in sites]
       
        for i, (site, icem) in enumerate(zip(sites, icems)):
            bewonersdata = {
                'aanhef_bewoner':None,
                'achternaam_bewoner':None,
                'voorletters_bewoner' : None,
                'phone_bewoner':None,
                'tussenvoegsels_bewoner':None,
                'email_bewoner':None,
                'site': site,
            }
            bewoner = Bewoners(**bewonersdata)
            bewoner = self.bewonerAanmaken(bewonersdata)
            allBewoners.append(bewoner)
       
            bouwkundigdata = {
                    'site' : site,
                    'nokHoogte': None,
                    'nokDiepte': None,
                    'typeDak': None,
                    'positieBuitendeel': None
                }
            bouwkundig = Bouwkundig(**bouwkundigdata)
            allBouwkundig.append(bouwkundig)
            #bouwkundig = self.bouwkundigAanmaken(bouwkundigdata)  
            
            # Planning Aanmaken
            planningdata = {
                'icem': icem,
                'bouwrouting':i+1,
                'leverdatum':None,
            }
            planning = Planning(**planningdata)
            #planning = self.planningAanmaken(planningdata)
            allPlanning.append(planning)
            # Boiler Aanmaken
            boilerdata = {
                'icem': icem,
                'inhoud': None
                } 
            #boiler = self.boilerAanmaken(boilerdata)
            boiler = Boiler(**boilerdata)
            allBoilers.append(boiler)
            #   Wtw Aanmaken
            wtwdata = {
                'icem': icem,
                'merk': None,
                'type': None,
                'debiet': None
            }
            #wtw = self.wtwAanmaken(wtwdata)
            wtw = WTW(**wtwdata)
            allWtw.append(wtw)
            # Warmte pomp Aanmaken
            warmtepompdata = {
                'icem': icem,
                'vermogen': None
                }
            #warmtepomp = self.warmtepompAanmaken(warmtepompdata)
            warmtepomp = Warmtepomp(**warmtepompdata)
            allWarmtepompen.append(warmtepomp)
            # Semkast Aanmaken
            semkastdata = {
                'icem': icem,
                'type': None
            }
            
            #semkast = self.semkastAanmaken(semkastdata)
            semkast = Semkast(**semkastdata)
            allSemkasten.append(semkast)
            # Icem debiet Aanmaken
            icemdebietdata = {
                'icem': icem,
                'stand1': None,
                'stand2': None,
                'stand3': None,
                'stand4': None,
                'stand5': None
            }
            #icemdebiet = self.icemdebietAanmaken(icemdebietdata)
            icemdebiet = IcemDebiet(**icemdebietdata)
            allIcemdebieten.append(icemdebiet)
            # Productie aanmaken
            productiedata = {
                'icem': icem,
                'bomId': None,
                'exactnummer':None,
            }
            #productieExact = self.productieAanmaken(productiedata)
            productieExact = ProductieExact(**productiedata)
            allProductieExact.append(productieExact)
            # Omvomermer aanmaken
            omvormerdata = {
                'icem': icem,
                'merkOmvormer': None,
                'dakheling': None,
                'owner': None,
                'capaciteit': None,
                'levering_datum': None,
                'levering_door': None,
            }

            productiebondata = {
                "icem": icem,
                "productiegereed": None,
                "productieDatum": None,
            }
            productieBon = ProductiebonStatus(**productiebondata)
            allProductieBon.append(productieBon)

            omvormer = Omvormer(**omvormerdata)
            omvormers.append(omvormer)
        Bewoners.objects.bulk_create(allBewoners, ignore_conflicts=True)
        Bouwkundig.objects.bulk_create(allBouwkundig)
        Planning.objects.bulk_create(allPlanning)
        Boiler.objects.bulk_create(allBoilers)
        WTW.objects.bulk_create(allWtw)
        Warmtepomp.objects.bulk_create(allWarmtepompen)
        Semkast.objects.bulk_create(allSemkasten)
        IcemDebiet.objects.bulk_create(allIcemdebieten)
        ProductieExact.objects.bulk_create(allProductieExact)
        ProductiebonStatus.objects.bulk_create(allProductieBon)
        Omvormer.objects.bulk_create(omvormers)

class UpdateMPO(APIView):

    # FUNCTIE BEWONERS AANMAKEN
    def bewonerAanmaken(self,data):
        try:
            bewoner = Bewoners.objects.create(**data)
            bewoner.save()
            return bewoner
        except Exception as e:
            return str(e)
    
    def siteAanmaken(self,data):
        try:
            site = Site.objects.create(**data)
            site.save()
            return site
        except Exception as e:
            return str(e)
    def productieAanmaken(self,data):

        try:
            productie = ProductieExact.objects.create(**data)
            productie.save()
            return productie
        except Exception as e:
            return str(e)

    def omvormerAanmaken(self,data):
        
        try:
            omvormer = Omvormer.objects.create(**data)
            omvormer.save()
            return omvormer
        except Exception as e:
            return str(e)

    def icemdebietAanmaken(self,data):
        try:
            icemdebiet = IcemDebiet.objects.create(**data)
            icemdebiet.save()
            return icemdebiet
        except Exception as e:
            return str(e)
    
    def semkastAanmaken(self,data):
        try:
            semkast = Semkast.objects.create(**data)
            semkast.save()
            return semkast
        except Exception as e:
            return str(e)
            
    def warmtepompAanmaken(self,data):
        try:
            warmtepomp = Warmtepomp.objects.create(**data)
            warmtepomp.save()
            return warmtepomp
        except Exception as e:
            return str(e)

    def wtwAanmaken(self,data):
        try:
            wtw = WTW.objects.create(**data)
            wtw.save()
            return wtw
        except Exception as e:
            return str(e)

    def boilerAanmaken(self,data):
        try:
            boiler = Boiler.objects.create(**data)
            boiler.save()
            return boiler
        except Exception as e:
            return str(e)

    def planningAanmaken(self,data):
        try:
            planning = Planning.objects.create(**data)
            planning.save()
            return planning
        except Exception as e:
             return str(e)

    def getprojectId(self,projectnummer):
        project = Project.objects.filter(projectnr=projectnummer).get()
        return project

    def IcemAanmaken(self,data): 
        try:
            icem = Icem.objects.create(**data)
            icem.save()
            return icem
        except Exception as e:
            return str(e)

    def bouwkundigAanmaken(self, data):
        try:
            bouwkundig = Bouwkundig.objects.create(**data)
            bouwkundig.save()
            return bouwkundig
        except Exception as e:
            return str(e)
    
    def returnThisOwner(self,e):
            if type(e) != str :
                if e == True:
                    x = 1
                    return x
                else:
                    x = 0
                    return x
            else:
                if e == "Klant":
                    x = 1
                    return x
                else:
                    x = 0
                    return x

    def returnThisLeveringdoor(self,e):
        if type(e) != str :
            if e == True:
                x = 1
                return x
            else:
                x = 0
                return x
        else:
            if e == "Ja":
                x = 1
                return x
            else:
                x = 0
                return x

    def update_sites(self,project,sitegegevens):
        sitesarray = []
        
        try:
            site_to_update = Site.objects.filter(projectId_id=project).order_by('id')
            print(f'got {site_to_update} sites to update')
            with transaction.atomic():
                for i,value in enumerate(site_to_update):
                    sitegegevens[i]['blok'] = sitegegevens[i]['blok'].upper() if sitegegevens[i]['blok'] is not None else None
                    Site.objects.filter(id=value.id).update(**sitegegevens[i])
                    site = Site.objects.get(id=value.id)
                    sitesarray.append(site)
            print(sitesarray)
            return sitesarray
        except Exception as e:
            return str(e)
    

    def update_icems(self,sites,data):
        all_icems = []
        
        with transaction.atomic():
            for i,site in enumerate(sites):
                icemdata = {
                    'icemType': data[i]['icemType'],
                    'energieModule':  data[i]['energieModule'],
                    'positieIcem': data[i]['links_rechts'],
                    'aansluitingkanalen':data[i]['aansluitingkanalen'],
                    'kwh_meter': data[i]['kwh_meter'],
                    'koeling': data[i]['koeling'],
                    'positieWPmodule': data[i]['positieWpModule'],
                    'sensoringOptie': data[i]['sensoringOptie'],
                    'type_prestatie': data[i]['typePrestatie'],
                }
                Icem.objects.filter(site=site).update(**icemdata)
                icem = Icem.objects.get(site=site)
                all_icems.append(icem.site_id)
        print('icems',all_icems)
        return all_icems

    def get_digital_uit_string(self,string):
        string_ = ''
        if string !='' and string !=None:
            if isinstance(string,int):
                string_ = string
            else:
                string_ = int(list(filter(str.isdigit, string))[0])
        else:
            string_ = None
        return string_
    
    def check_if_owner_true(self,string):
        if string == 'Klant':
            return True
        else:
            return False
        
    def returnIntValue(self,value):
        if value == '' or value == None:
            return None
        else:
            return int(value)
    def post(self, request, format=None):
        dataAll = self.request.data
        project = getProject(dataAll['projectId'])
        sites = self.update_sites(project,dataAll['algemeene'])
        icemgegevens = dataAll['icemComponenten']
        icems = self.update_icems(sites,icemgegevens)
        databewoners = dataAll['bewoners']
        dataOmvormer = dataAll['omvormer']
        dataIcemdebiet = dataAll['icemDebiet']
        dataPlanning = dataAll['planning']
        dataBouwkundig = dataAll['bouwkundig']
        dataProductie_exact = dataAll['productie_exact']
        try:
            with transaction.atomic():
                for i, (site,icem) in enumerate(zip(sites,icems)):
                
                    wtwdata = {
                        'merk': icemgegevens[i]['merkWtw'],
                        'type': icemgegevens[i]['typeWtw'],
                        'debiet': icemgegevens[i]['wtwDebiet']
                    }
                    
                    try:
                        WTW.objects.filter(icem=icem).update(**wtwdata)
                    except Exception as e:
                        print(e)
                        return str(e)
                    warmtepompdata = {
                        'vermogen': self.get_digital_uit_string(icemgegevens[i]['vermogenWp'])
                    }
                    try:
                        Warmtepomp.objects.filter(icem=icem).update(**warmtepompdata)
                    except Exception as e:
                        return str(e)
                    semkastdata = {
                        'type': icemgegevens[i]['semkast']
                    }
                    try:
                        Semkast.objects.filter(icem=icem).update(**semkastdata)
                    except Exception as e:
                        return str(e)
                    
                    
                    boilerdata = {
                        'inhoud': icemgegevens[i]['boilerInhoud']
                    }
                    try:
                        Boiler.objects.filter(icem=icem).update(**boilerdata)
                    except Exception as e:
                        return str(e)
                    omvormerdata = {
                        'merkOmvormer': dataOmvormer[i]['omvromerMerk'],
                        'dakheling': icemgegevens[i]['dakhelling'] ,
                        'owner': dataOmvormer[i]['omvormerOwner'],
                        'capaciteit': dataOmvormer[i]['capaciteit'],
                        'levering_datum': dataOmvormer[i]['levering_datum'],
                        'levering_door': dataOmvormer[i]['levering_door'],
                    }
                    try:
                        Omvormer.objects.filter(icem=icem).update(**omvormerdata)
                    except Exception as e:
                       return str(e)
                   
                    icemdebietdata = {
                        'stand1': dataIcemdebiet[i]['stand1'],
                        'stand2': dataIcemdebiet[i]['stand2'],
                        'stand3': dataIcemdebiet[i]['stand3'],
                        'stand4': dataIcemdebiet[i]['stand4'],
                        'stand5': dataIcemdebiet[i]['stand5'],
                    }
                    try:
                        IcemDebiet.objects.filter(icem=icem).update(**icemdebietdata)
                    except Exception as e:
                        return str(e)

                    planningdata = {
                        'bouwrouting': site.bouwnr,
                        'leverdatum': dataPlanning[i]['leverdatum']
                    }
                    try:
                        Planning.objects.filter(icem=icem).update(**planningdata)
                    except Exception as e:
                        return str(e)
                    
                    bouwkundigdata = {
                        'nokHoogte': self.returnIntValue(dataBouwkundig[i]['nokHoogte']),
                        'nokDiepte': self.returnIntValue(dataBouwkundig[i]['nokDiepte']),
                        'typeDak': dataBouwkundig[i]['typeDak'],
                        'positieBuitendeel': dataBouwkundig[i]['positiebuitendeel']
                    }
                    try:
                        Bouwkundig.objects.filter(site=site).update(**bouwkundigdata)
                    except Exception as e:
                        return str(e)

                    productie_exact = {
                        'bomId': dataProductie_exact[i]['bomId'],
                        'exactnummer': dataProductie_exact[i]['exactnummer']

                    }
                    try:
                        ProductieExact.objects.filter(icem=icem).update(**productie_exact)
                    except Exception as e:
                        return str(e)
                    
                    bewonersdata = {
                        'aanhef_bewoner': databewoners[i]['aanhef'],
                        'achternaam_bewoner': databewoners[i]['achternaam'],
                        'voorletters_bewoner': databewoners[i]['voorletter'],
                        'phone_bewoner': databewoners[i]['phone'],
                        'tussenvoegsels_bewoner': databewoners[i]['tussenvoegsel'],
                        'email_bewoner': databewoners[i]['email']
                    }
                    Bewoners.objects.filter(site=site).update(**bewonersdata)
            return Response({'success': True})
        except Exception as e:
            print(e)
            return Response({'error': str(e)})

        

def getSitequeryset(id,projectid):
    site = Site.objects.filter(id=id,projectId_id=projectid).get()
    return site.bouwnr
def get_querry_set():
        productieStatus = ProductiebonStatus.objects.all()
        return productieStatus
def get_opdrachtgever(id):
    opdrachtgever = {}
    opdrachtgever = Klant.objects.filter(pk=id).values('id','klantnaam')
    return opdrachtgever
def checkValueIsnull(value):
    if value == None:
        return ''
    else:
        return value
class Getproductiebon(APIView):
    
    def post(self, request,format=None):
        data = self.request.data
        project = getProject(data)
        sites = Site.objects.filter(projectId_id = project).order_by('id')
        siteIds = sites.values_list('id',flat=True)
        icems = Icem.objects.in_bulk(list(siteIds))
        preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(icems)])
        icemIds = Icem.objects.filter(pk__in=icems).order_by(preserved)
        icems = [v for k, v in icems.items()]
        planningen= Planning.objects.in_bulk(list(icemIds))
        productiebonstatus = ProductiebonStatus.objects.in_bulk(list(icemIds))
        boiler = Boiler.objects.in_bulk(list(icemIds))
        warmtepompen = Warmtepomp.objects.in_bulk(list(icemIds))
        wtws = WTW.objects.in_bulk(list(icemIds))
        omvormers = Omvormer.objects.in_bulk(list(icemIds))
        semkasten = Semkast.objects.in_bulk(list(icemIds))
        icemdebiten = IcemDebiet.objects.in_bulk(list(icemIds))
        planningen= [v for k, v in planningen.items()]
        productiebonstatus = [v for k, v in productiebonstatus.items()]
        boiler = [v for k, v in boiler.items()]
        warmtepompen = [v for k, v in warmtepompen.items()]
        wtws = [v for k, v in wtws.items()]
        omvormers = [v for k, v in omvormers.items()]
        semkasten = [v for k, v in semkasten.items()]
        icemdebiten = [v for k, v in icemdebiten.items()]
        sitearray = []
        for site,icem,planning,productiebonstatuss,boil,warmtepomp,wtw,omvormer,semkast,icemdebiet in zip(sites,icems,planningen,productiebonstatus,boiler,warmtepompen,wtws,omvormers,semkasten,icemdebiten):
            sitearray.append(
                {
                'blok':site.blok,
                'bouwnr': site.bouwnr,
                'adres': checkValueIsnull(site.straat) + checkValueIsnull(site.huisnr),
                'icemType': icem.icemType,
                'icem': checkValueIsnull(icem.energieModule) + checkValueIsnull(icem.icemType) + checkValueIsnull(icem.positieIcem),
                'productiegereed': productiebonstatuss.productiegereed,
                'productieDatum': productiebonstatuss.productieDatum,
                'leverdatum': planning.leverdatum,
                'printdata': {
                    'projectnr': project.projectnr,
                    'projectnaam': project.projectnaam,
                    'orderexact': project.exactnr,
                    'energieModule': checkValueIsnull(icem.energieModule),
                    'icemType': checkValueIsnull(icem.icemType),
                    'icemPositie': checkValueIsnull(icem.positieIcem),
                    'leverdatum': planning.leverdatum,
                    'bouwnr': site.bouwnr,
                    'blok':site.blok,
                    'straat': checkValueIsnull(site.straat),
                    'nummer': checkValueIsnull(site.huisnr),
                    'postcode': checkValueIsnull(site.postcode),
                    'plaats': checkValueIsnull(project.plaats),
                    'boiler': checkValueIsnull(boil.inhoud),
                    'wp': checkValueIsnull(warmtepomp.vermogen),
                    'koeling': checkValueIsnull(icem.koeling),
                    'ventilatie_merk': checkValueIsnull(wtw.merk),
                    'ventilatie_type': checkValueIsnull(wtw.type),
                    'omvormer_merk': checkValueIsnull(omvormer.merkOmvormer),
                    'omvormer_capaciteit': checkValueIsnull(omvormer.capaciteit),
                    'semkast_type': checkValueIsnull(semkast.type),
                    'sensoring': checkValueIsnull(icem.sensoringOptie),
                    'dakheling': checkValueIsnull(omvormer.dakheling),
                    'aansluitingkanalen': checkValueIsnull(icem.aansluitingkanalen),
                    'ventilatie_debieten': {
                        'stand_1': checkValueIsnull(icemdebiet.stand1),
                        'stand_2': checkValueIsnull(icemdebiet.stand2),
                        'stand_3': checkValueIsnull(icemdebiet.stand3),
                        'stand_4': checkValueIsnull(icemdebiet.stand4),
                        'stand_5': checkValueIsnull(icemdebiet.stand5),
                    },
                    'bijzonderheden': checkValueIsnull(site.bijzonderheden),

                }
                }
            )

        contextObject = {
            'projectnaam':project.projectnaam,
            'projectnr': project.projectnr,
            'opdrachtgever': get_opdrachtgever(project.pk),
            'plaats': project.plaats,
            'provincie': project.provincie,
            'sitesgegevens': sitearray
        }
      
        return Response({
            'data': contextObject
        })
        
class GetProductieStatus(APIView):
    
    def post(self, request,format=None):
        data = self.request.data
        try:
            if data != None and data !={}:
                result = self.getResults(data['id'])
                return Response({'data': result})
            else:
                return Response({'error': data})
        except Exception as e:
            return Response({'error': str(e)})
    def getResults(self,projectId):
        productiebonstatus = list(get_querry_set())
        idProject = projectId
        bouwnr = []
        printDatum = []
        productieDatum = []
        count = []
        context = {
            'bouwnr': bouwnr,
            'printDatum': printDatum,
            'productieDatum': productieDatum,
            'count':count
        }
        for i in productiebonstatus:
            site_bouwnummer = getSitequeryset(i.site_id,idProject)
            bouwnr.append(site_bouwnummer)
            printDatum.append(i.printDatum)
            productieDatum.append(i.productieDatum)
            count.append(i.count)
        return context
class CreateProductieStatus(APIView):
    def post(self,request,format=None):
        data = self.request.data
        bouwnr = data['bouwnr']
        projectId = data['projectId']
        # get the siteId
        site = Site.objects.filter(bouwnr=bouwnr,projectId_id=projectId).get()

        # check if site existe and update
        
        try:
            if ProductiebonStatus.objects.filter(bouwnr=bouwnr).exists():
        
                productiequeryset = ProductiebonStatus.objects.filter(bouwnr=bouwnr).get()
                count = 0
                if productiequeryset.count == None:
                    count = 0
                else:
                    count = productiequeryset.count
                dataToOpslaan ={
                'printDatum':data['printDatum'],
                'productieDatum': data['productieDatum'],
                'count': int(count) + 1
                } 
                ProductiebonStatus.objects.filter(bouwnr=bouwnr).update(**dataToOpslaan)
                return Response({'success': 'succesfully updated'})

            else:
                dataToOpslaan ={
                    'printDatum':data['printDatum'],
                    'site_id': site.id,
                    'bouwnr': bouwnr,
                    'productieDatum': data['productieDatum'],
                    'count': 1
                    } 
                try:
                    ProductiebonStatus.objects.create(**dataToOpslaan)
                    return Response({'success': 'succesfully updated'})
                except Exception as e:
                    return Response(str(e))
        except Exception as e:
            return Response({'error': str(e)})

class GetDataToPrint(APIView):
    def post(self,request,format=None):
        data = self.request.data
   
