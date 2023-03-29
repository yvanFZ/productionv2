from django.db import models
# from leads.models import Lead, Icem
from users.models import MedewerkerProfile

# Create your models here.

class Klant(models.Model):
    klantnaam = models.CharField(max_length=30,null=False,default=False)
    plaats = models.CharField(max_length=30,null=False,default=False)
    land = models.CharField(max_length=30,null=False,default=False)
    provincie = models.CharField(max_length=30,null=False,default=False)
    phone = models.CharField(max_length=30,null=False,default=False)

    def __str__(self):
        return f"{self.klantnaam}"

class KlantMedewerker(models.Model):
    name_medewerker = models.CharField(max_length=30,null=False,default=False)
    achternaam_medewerker = models.CharField(max_length=30,null=False,default=False)
    phone = models.CharField(max_length=30,null=False,default=False)
    functie_medewerker = models.CharField(max_length=30,null=False,default=False)
    klantID = models.ForeignKey(Klant,default=False,null=False, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name_medewerker}"

class Project(models.Model):
    projectnr = models.CharField(unique=True,max_length=30,null=False,default=False)
    projectnaam = models.CharField(max_length=50,null=False,default=False,blank=False)
    plaats = models.CharField(max_length=15,null=False,default=False,blank=False)
    provincie = models.CharField(max_length=15,null=False,default=False,blank=False)
    land = models.CharField(max_length=15,null=False,default=False,blank=False)
    klant = models.ForeignKey(Klant,default=False,null=False, on_delete=models.CASCADE)
    projectStatus = models.CharField(max_length=15,null=False,default=False,blank=False)
    offertenr = models.CharField(max_length=30,null=True,default=True,blank=True)
    exactnr = models.CharField(max_length=30,null=True,default=True,blank=True)
    debiteurnr = models.CharField(max_length=30,null=True,default=True,blank=True)
    renovatie_nieuwbouw = models.CharField(max_length=15,null=True,default=True,blank=True)
    selectedProjectleiderAanmelder = models.IntegerField(null=True,default=True,blank=True)
    selectedWerkvoorbereiderAanmelder = models.IntegerField(null=True,default=True,blank=True)
    selectedUitvoerderAanmelder = models.IntegerField(null=True,default=True,blank=True)
    selectedWerkvoorbereiderFz = models.IntegerField(null=True,default=True,blank=True)
    selectedProjecleiderFz = models.IntegerField(null=True,default=True,blank=True)
    inopdrachtvoor_vloerverwarming = models.CharField(max_length=15,null=True,default=True,blank=True)
    inopdrachtvoor_ventilatieinstallatie = models.CharField(max_length=15,null=True,default=True,blank=True)
    inopdrachtvoor_zonnepanelen = models.CharField(max_length=15,null=True,default=True,blank=True)
    datumSystemInvoer = models.CharField(max_length=30,null=True,default=True,blank=True)
    startDatum = models.CharField(max_length=30,null=True,default=True,blank=True)
    offertedatum = models.CharField(max_length=30,null=True,default=True,blank=True)   
    uitlijkDatumOpdrachtIndienWTW = models.CharField(max_length=30,null=True,default=True,blank=True)
    uitlijkDatumOpdrachtAlleenICEM = models.CharField(max_length=30,null=True,default=True,blank=True)
    opmerking = models.CharField(max_length=255,null=True,default=True,blank=True)

    def __str__(self):
        return f"{self.projectnaam}"

class ProjectIcem(models.Model):
    iNumber = models.CharField(max_length=10,default=False,null=False)
    pNumber = models.CharField(max_length=10,default=False,null=False)
    eNumber = models.CharField(max_length=10,default=False,null=False)
    fNumber = models.CharField(max_length=10,default=False,null=False)
    aNumber = models.CharField(max_length=10,default=False,null=False)
    totaalNumber = models.CharField(max_length=20,default=False,null=False)
    estimatedValue = models.CharField(max_length=20,default=False,null=False)
    project = models.ForeignKey(Project,default=False,null=False, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.project}"

class Onderaanemerbedrijf(models.Model):
    naam = models.CharField(max_length=30,null=False,default=False)

class StatusOnderaanemer(models.Model):
    status = models.CharField(max_length=30,null=False,default=False)
    onderaanemer = models.ForeignKey(Onderaanemerbedrijf,default=False,null=True, on_delete=models.CASCADE)
    odernummer =  models.CharField(max_length=30,null=False,default=False)
    project_id = models.ForeignKey(Project,default=False,null=True, on_delete=models.CASCADE) 
    
class Vertegenwoordiger_Project(models.Model):
    vertegenwoordiger = models.ForeignKey(MedewerkerProfile,null=False, default=False, blank=False,on_delete=models.CASCADE)
    projectnr = models.CharField(max_length=30,default=False, unique=False)

    def __str__(self):
        return f"{self.projectnr}"

