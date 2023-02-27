
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import serializers
from project.models import Project
from .models import Site,ProductieExact,Omvormer,IcemDebiet,Semkast,Warmtepomp, WTW,Boiler,Planning,Icem,Bouwkundig,Bewoners,ProductiebonStatus
import json
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
        #  return Site.objects.filter(projectId_id = id).get()
        #  if Site.objects.filter(projectId_id = id).exists():
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
        icemComponenten = []
        icemDebiet = []
        omvormer = []
        planning = []
        bouwkundig = []
        productieExact = []
        bewoner = []
        jsonData = {
            'algemeene': algemeneObject,
            'icemComponenten':icemComponenten,
            'icemDebiet': icemDebiet,
            'omvormer':omvormer,
            'planning': planning,
            'bouwkundig': bouwkundig,
            'productieExact': productieExact,
            'bewoner': bewoner

        }
         # Site gegevens
        for site in Site.objects.filter(projectId_id=(projectID)):
            # Icem gegevens
            icemdata = Icem.objects.filter(id = site.icemId_id).get()
            # Boiler gegevens
            idboiler = icemdata.boiler_Id_id
            boilerdata = Boiler.objects.filter(id=idboiler).get()
             # WP gegevens
            idWP = icemdata.warmtepompId_id
            wPdata = Warmtepomp.objects.filter(id=idWP).get()
             # Omvormer gegevens
            idOmvormer = icemdata.omvormerId_id
            omvormerdata = Omvormer.objects.filter(id=idOmvormer).get()
             # Icemdebiet gegevens
            idIcemdebiet = icemdata.icemDebietId_id
            icemdebietdata = IcemDebiet.objects.filter(id=idIcemdebiet).get()
            #Semkast gegevens
            idSemkast = icemdata.semkastId_id
            semkastdata = Semkast.objects.filter(id=idSemkast).get()
             # WTW gegevens
            idWtw = icemdata.wtw_Id_id
            wtwdata = WTW.objects.filter(id=idWtw).get()
             # Planning gegevens
            idPlanning = icemdata.planningId_id
            planningdata = Planning.objects.filter(id=idPlanning).get()
            #Bouwkundig gegevens
            bouwkundigdata = Bouwkundig.objects.filter(id = site.bouwkundigId_id).get()
             #Productie Exact
            productieexactId = icemdata.productieExactId_id
            productiedata = ProductieExact.objects.filter(id=productieexactId).get()
             # Bewoner gegevens
            bewonerdata = Bewoners.objects.filter(siteId_id=site.id).get()

            algemeneObject.append({
                'blok': site.blok,
                'straat': site.straat,
                'huisnr': site.huisnr,
                'postcode': site.postcode,
                'bijzonderheden': site.bijzonderheden,
                'koop_huur':site.koop_huur
            })
            
            icemComponenten.append(
                {
                'blok': site.blok,
                'icemType': icemdata.icemType,
                'energieModule': icemdata.energieModule,
                'dakhelling': omvormerdata.dakheling,
                'links_rechts': icemdata.positieIcem,
                'aansluitingkanalen': icemdata.aansluitingkanalen,
                'boilerInhoud': boilerdata.inhoud,
                'merkWtw': wtwdata.merk,
                'typeWtw': wtwdata.type,
                'wtwDebiet': wtwdata.debiet,
                'vermogenWp': wPdata.vermogen,
                'kwh_meter': icemdata.kwh_meter,
                'semkast': semkastdata.type,
                'sensoringOptie': icemdata.sensoringOptie,
                'typePrestatie': icemdata.type_prestatie,
                'koeling': icemdata.koeling,
                'positieWpModule': icemdata.positieWPmodule,

            })
            
            icemDebiet.append({
                'stand1': icemdebietdata.stand1,
                'stand2': icemdebietdata.stand2,
                'stand3': icemdebietdata.stand3,
                'stand4': icemdebietdata.stand4,
                'stand5': icemdebietdata.stand5,

            })
            
            omvormer.append({
                'omvormerOwner': omvormerdata.owner,
                'omvromerMerk': omvormerdata.merkOmvormer,
                'capaciteit': omvormerdata.capaciteit,
                'levering_door': omvormerdata.levering_door,
                'levering_datum': omvormerdata.levering_datum
            })
           
            planning.append({
                'bouwrouting': planningdata.bouwrouting,
                'leverdatum': planningdata.leverdatum
            })
            
            
            bouwkundig.append({
                'nokHoogte': bouwkundigdata.nokHoogte,
                'nokDiepte': bouwkundigdata.nokDiepte,
                'typeDak': bouwkundigdata.typeDak,
                'positiebuitendeel': bouwkundigdata.positieBuitendeel
            })
            
            productieExact.append({
                'bomId': productiedata.bomId,
                'exactnummer': productiedata.exactnummer
            })
            
            bewoner.append(
                {
                'aanhef': bewonerdata.aanhef_bewoner,
                'achternaam': bewonerdata.achternaam_bewoner,
                'voorletter': bewonerdata.voorletters_bewoner,
                'phone': bewonerdata.phone_bewoner,
                'tussenvoegsel': bewonerdata.tussenvoegsels_bewoner,
                'email': bewonerdata.email_bewoner
                
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
        else:
            error = "Create project first"
            return Response({'error':error})
        # re.findall(r'\d+', projectnaam)
        mpo_leng = int(re.findall(r'\d+', projectnaam)[0])
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
                    'bouwrouting':i+1,
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
       
    def post(self,request,format=None):
        projectID = self.request.data
        
        try:
        
            if Site.objects.filter(projectId_id = projectID).exists():
                data = self.getAllmpoData(projectID)
                return Response({'data': data})
            else: 
                if self.createMPO(projectID):
                    data = self.getAllmpoData(projectID)
                    return Response({'data': data})
                else:
                    print("error")
            
        except Exception as e:
            print(e)
    # CREATE

class CreateMPO(APIView):

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
    
    def create(self,dataAll):
        msg = ''
        for data in dataAll:
            mpodata = data['mpodata']
            projectnr = data.get('projectnummer', {}).get('projectnummer')

            if Site.objects.filter(projectId_id = self.getprojectId(projectnr),bouwnr=mpodata["Bouwnr"]).exists():
                # UPDATDE
                
                try:
                    # update site
                    site = Site.objects.filter(projectId_id = self.getprojectId(projectnr),bouwnr=mpodata['Bouwnr']).update(
                        blok=mpodata['Blok'],huisnr=mpodata['Huisnr'],bijzonderheden=mpodata['Bijzonderheden'],
                        koop_huur=mpodata['Koop/Huur'],postcode=mpodata['Poscode'],straat=mpodata['Straat']
                    )
                    siteInstance = Site.objects.filter(projectId_id = self.getprojectId(projectnr),bouwnr=mpodata['Bouwnr']).get()
        
                    # update bewoner
                    Bewoners.objects.filter(siteId_id=siteInstance.id).update(
                        aanhef_bewoner=mpodata['Aanhef'],achternaam_bewoner=mpodata['Achternaam'],
                        tussenvoegsels_bewoner = mpodata['Tussenvoegsels'],phone_bewoner=mpodata['Telefoon'],
                        email_bewoner= mpodata['Email'],voorletters_bewoner=mpodata['Voorletters']
                    )
                    # update bouwkundig
                    boukundinokhoogte = getDigitOutString(mpodata['Nok hoogte'])
                    bouwkundignokdiepte = getDigitOutString(mpodata['Diepte woning'])
                    Bouwkundig.objects.filter(id=siteInstance.bouwkundigId_id).update(
                        nokHoogte = boukundinokhoogte,nokDiepte = bouwkundignokdiepte,
                        positieBuitendeel = mpodata['Positie buitendeel'],typeDak=mpodata['Type dak']
                    )
                    # get icemdata's
                    Icem.objects.filter(id=siteInstance.icemId_id).update(
                        icemType = mpodata['Icem type'],
                        energieModule = mpodata['Energiemodule'],
                        positieIcem = mpodata['Positie Icem'],
                        aansluitingkanalen = mpodata['Aansluiting kanalen'],
                        kwh_meter = mpodata['Kwh-Meter'],
                        koeling = mpodata['Koeling'],
                        positieWPmodule = mpodata['Positie wp module'],
                        sensoringOptie = mpodata['Sensoring optie'],
                        type_prestatie = mpodata['Type prestatie']
                    )
                    icemInstance = Icem.objects.filter(id=siteInstance.icemId_id).get()
                
                    # update planning
                    Planning.objects.filter(id=icemInstance.planningId_id).update(
                        leverdatum= mpodata['Levering module']
                    )
                    #update Boiler
                    try:
                        Boiler.objects.filter(id=icemInstance.boiler_Id_id).update(
                            inhoud = getDigitOutString(mpodata['Boiler'])
                    )
                    except Exception as e:
                        print(e)
                    
                    #update WTW
                    WTW.objects.filter(id=icemInstance.wtw_Id_id).update(
                        merk = mpodata['Merk-Wtw'],type=mpodata['Type-Wtw'],
                        debiet= mpodata['Wtw-debieten']
                    )
                    # update Warmte Pomp
                    Warmtepomp.objects.filter(id=icemInstance.warmtepompId_id).update(
                        vermogen  = getDigitOutString(mpodata['Vermogen-wp'])
                    )
                    #update semkast
                    Semkast.objects.filter(id=icemInstance.semkastId_id).update(
                        type=mpodata['Semkast']
                    )               
                    #update Productie Exact
                    print(mpodata['Bom Id'])
                    ProductieExact.objects.filter(id=icemInstance.productieExactId_id).update(
                        bomId = getDigitOutString(mpodata['Bom Id']),exactnummer=getDigitOutString(mpodata['Werknr exact'])
                    )
                    #update Omvormer
                    Omvormer.objects.filter(id=icemInstance.omvormerId_id).update(
                        merkOmvormer=mpodata['Merk omvormer'],dakheling=mpodata['Dak helling'],
                        capaciteit=getDigitOutString(mpodata['Capaciteit']),owner=self.returnThisOwner(mpodata['Omvormer Fz/Klant']),
                        levering_door=self.returnThisLeveringdoor(mpodata['Levering door klant']),levering_datum=mpodata['Levering datum omvormer']
                    )
                    #update Icemdebiet
                    IcemDebiet.objects.filter(id=icemInstance.icemDebietId_id).update(
                        stand1=mpodata['Stand 1'],stand2=mpodata['Stand 2'],stand3=mpodata['Stand 3'],
                        stand4=mpodata['Stand 4'],stand5=mpodata['Stand 5']
                    )
                    
                    msg = 'updated'      
                except Exception as e:
                    return Response({'error': str(e)}) 
            else:
                # create mpo tables
                bouwkundigdata = {
                    'nokHoogte': getDigitOutString(mpodata['Nok hoogte']),
                    'nokDiepte': getDigitOutString(mpodata['Diepte woning']),
                    'typeDak': mpodata['Type dak'],
                    'positieBuitendeel': mpodata['Positie buitendeel']
                }
                # Planning Aanmaken
                planningdata = {
                    'bouwrouting':mpodata['Bouwrouting'],
                    'leverdatum':mpodata['Levering module'],
                }
                # Boiler Aanmaken
                boilerdata = {
                    'inhoud': getDigitOutString(mpodata['Boiler'])
                    } 
                #   Wtw Aanmaken
                wtwdata = {
                    'merk': mpodata['Merk-Wtw'],
                    'type': mpodata['Type-Wtw'],
                    'debiet': mpodata['Wtw-debieten']
                }
                # Warmte pomp Aanmaken
                warmtepompdata = {
                    'vermogen': getDigitOutString(mpodata['Vermogen-wp'])
                    }
                # Semkast Aanmaken
                semkastdata = {
                    'type': mpodata['Semkast']
                }
                # Icem debiet Aanmaken
                icemdebietdata = {
                    'stand1': mpodata['Stand 1'],
                    'stand2': mpodata['Stand 2'],
                    'stand3': mpodata['Stand 3'],
                    'stand4': mpodata['Stand 4'],
                    'stand5': mpodata['Stand 5']
                }
                # Productie aanmaken
                productiedata = {
                    'bomId': getDigitOutString(mpodata['Bom Id']),
                    'exactnummer': mpodata['Werknr exact'],
                }
                # Omvomermer aanmaken
                omvormerdata = {
                    'merkOmvormer': mpodata['Merk omvormer'],
                    'dakheling': mpodata['Dak helling'],
                    'owner': self.returnThisOwner(mpodata['Omvormer Fz/Klant']),
                    'capaciteit': getDigitOutString(mpodata['Capaciteit']),
                    'levering_datum': mpodata['Levering datum omvormer'],
                    'levering_door': self.returnThisLeveringdoor(mpodata['Levering door klant']),
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
                        'icemType' : mpodata['Icem type'],
                        'energieModule' : mpodata['Energiemodule'],
                        'positieIcem' : mpodata['Positie Icem'],
                        'aansluitingkanalen' : mpodata['Aansluiting kanalen'],
                        'kwh_meter' : mpodata['Kwh-Meter'],
                        'koeling' : mpodata['Koeling'],
                        'positieWPmodule' : mpodata['Positie wp module'],
                        'sensoringOptie' : mpodata['Sensoring optie'],
                        'type_prestatie' : mpodata['Type prestatie'],
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
                        'bouwnr': mpodata['Bouwnr'],
                        'blok': mpodata['Blok'],
                        'straat': mpodata['Straat'],
                        'huisnr': mpodata['Huisnr'],
                        'postcode': mpodata['Poscode'],
                        'bijzonderheden': mpodata['Bijzonderheden'],
                        'koop_huur': mpodata['Koop/Huur'],
                        'bouwkundigId_id': bouwkundigId.id,
                        'icemId_id':idIcem.id,
                        'projectId_id':self.getprojectId(projectnr).id,
                    }
                    site = self.siteAanmaken(sitedata)
                    bewonersdata = {
                    # DATA FOR BEWONERS
                    'aanhef_bewoner':mpodata['Aanhef'],
                    'achternaam_bewoner':mpodata['Achternaam'],
                    'voorletters_bewoner' : mpodata['Voorletters'],
                    'phone_bewoner':mpodata['Telefoon'],
                    'tussenvoegsels_bewoner':mpodata['Tussenvoegsels'],
                    'email_bewoner':mpodata['Email'],
                    'siteId_id': site.id,
                    }
                    bewoner = self.bewonerAanmaken(bewonersdata)
                    
                    msg = 'created'
     
                except Exception as e:
                    return str(e)
                
        return msg
    def post(self, request, format=None):
        dataAll = self.request.data
        msg = self.create(dataAll)
        if msg == "created":
            return Response({
                    'success': 'Mpo met success toegevoegd',
                    })
        elif msg == "updated":
            try: 

                return Response({
                    'success': 'Mpo met success bijgewerkt',
                    })
            except Exception as e:
                print(e)
                return Response({
                    'error': str(e)
                })
        else:
            Response({
                'error': 'Something went wrong'
            })
def getSitequeryset(id,projectid):
    site = Site.objects.filter(id=id,projectId_id=projectid).get()
    return site.bouwnr
def get_querry_set():
        productieStatus = ProductiebonStatus.objects.all()
        return productieStatus
class GetProductieStatus(APIView):
    
    def post(self, request,format=None):
        data = self.request.data
        print(data)
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
            # data.printDatum.append(i.printDatum)
            # data.productieDatum.append(i.productieDatum)
            # data.count.append(i.count)

        # jsondata = serializers.serialize("json",productiebonstatus)
        # dataObj = json.loads(jsondata)
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
        
