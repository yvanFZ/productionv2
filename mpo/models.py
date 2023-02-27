from django.db import models
from project.models import Project
import uuid
# Create your models here.


class Site(models.Model):
    # uniqueId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bouwnr = models.CharField(max_length=30,null=True,default=True)
    blok = models.CharField(max_length=30,null=True,default=True)
    straat = models.CharField(max_length=30,null=True,default=True)
    huisnr = models.CharField(max_length=10,null=True,default=True)
    postcode = models.CharField(max_length=10,null=True,default=True)
    bijzonderheden = models.TextField(null=True,default=False)
    koop_huur = models.CharField(max_length=30,null=True,default=True)
    projectId = models.ForeignKey(Project, on_delete=models.CASCADE,related_name="project")

    def __str__(self):
        return f"{self.bouwnr}"
class Icem(models.Model):
    site = models.OneToOneField(
        Site,
        on_delete=models.CASCADE,
        primary_key=True)
    icemType = models.CharField(max_length=2,null=True,default=True)
    energieModule = models.CharField(max_length=30,null=True,default=True)
    positieIcem = models.CharField(max_length=30,null=True,default=True)
    aansluitingkanalen = models.CharField(max_length=30,null=True,default=True)
    kwh_meter = models.CharField(max_length=30,null=True,default=True)
    sensoringOptie = models.CharField(max_length=255,null=True,default=True)
    type_prestatie = models.CharField(max_length=30,null=True,default=True)
    koeling = models.CharField(max_length=30,null=True,default=True)
    positieWPmodule = models.CharField(max_length=30,null=True,default=True)
    def __str__(self):
        return f"{self.icemType}"

class IcemDebiet(models.Model):
    stand1 = models.IntegerField(null=True,default=True)
    stand2 = models.IntegerField(null=True,default=True)
    stand3 = models.IntegerField(null=True,default=True)
    stand4 = models.IntegerField(null=True,default=True)
    stand5 = models.IntegerField(null=True,default=True)
    icem = models.OneToOneField(
        Icem,
        on_delete=models.CASCADE,
        primary_key=True)
    def __str__(self):
        return f"{self.icem}"

class Boiler(models.Model):
    # serienummerBoiler = models.CharField(max_length=30,null=True,default=True)
    inhoud = models.IntegerField(null=True,default=True)
    icem = models.OneToOneField(
        Icem,
        on_delete=models.CASCADE,
        primary_key=True)
    def __str__(self):
        return f"{self.icem}"

class Planning(models.Model):
    bouwrouting = models.IntegerField(null=True,default=True)
    leverdatum =models.CharField(max_length=30,null=True,default=True)
    icem = models.OneToOneField(
        Icem,
        on_delete=models.CASCADE,
        primary_key=True)
    def __str__(self):
        return f"{self.icem}"

class Omvormer(models.Model):
    merkOmvormer = models.CharField(max_length=30,null=True,default=True)
    dakheling = models.IntegerField(null=True,default=True)
    capaciteit = models.IntegerField(null=True,default=True)
    owner = models.BooleanField(null=True)
    levering_door = models.BooleanField(null=True)
    levering_datum = models.CharField(max_length=30,null=True,default=True)
    icem = models.OneToOneField(
        Icem,
        on_delete=models.CASCADE,
        primary_key=True)
    def __str__(self):
        return f"{self.icem}"

class Warmtepomp(models.Model):
    vermogen = models.FloatField(null=True,default=True)
    icem = models.OneToOneField(
        Icem,
        on_delete=models.CASCADE,
        primary_key=True)
    def __str__(self):
        return f"{self.icem}"

class ProductieExact(models.Model):

    bomId = models.IntegerField(null=True,default=True)
    exactnummer = models.IntegerField(null=True,default=True)
    icem = models.OneToOneField(
        Icem,
        on_delete=models.CASCADE,
        primary_key=True)
    def __str__(self):
        return f"{self.icem}"

class WTW(models.Model):
    merk = models.CharField(max_length=30,null=True,default=True)
    type = models.CharField(max_length=30,null=True,default=True)
    debiet = models.IntegerField(null=True,default=True)
    icem = models.OneToOneField(
        Icem,
        on_delete=models.CASCADE,
        primary_key=True)
    def __str__(self):
        return f"{self.icem}"

class Semkast(models.Model):
    type = models.CharField(max_length=30,null=True,default=True)
    icem = models.OneToOneField(
        Icem,
        on_delete=models.CASCADE,
        primary_key=True)
    def __str__(self):
        return f"{self.icem}"



class Bouwkundig(models.Model):
    nokHoogte= models.IntegerField(null=True,default=True)
    nokDiepte= models.IntegerField(null=True,default=True)
    typeDak= models.CharField(max_length=30,null=True,default=True)
    positieBuitendeel = models.CharField(max_length=30,null=True,default=True)
    site = models.OneToOneField(
        Site,
        on_delete=models.CASCADE,
        primary_key=True)

    def __str__(self):
        return f"{self.site}"

class Bewoners(models.Model):
    aanhef_bewoner= models.CharField(max_length=30,null=True,default=True)
    achternaam_bewoner = models.CharField(max_length=30,null=True,default=True)
    voorletters_bewoner = models.CharField(max_length=30,null=True,default=True)
    phone_bewoner = models.CharField(max_length=30,null=True,default=True)
    tussenvoegsels_bewoner = models.CharField(max_length=30,null=True,default=True)
    email_bewoner = models.EmailField(unique=True,default=True,null=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE,related_name="sitebewoner")

    def __str__(self):
        return f"{self.achternaam_bewoner}"

class ProductiebonStatus(models.Model):
    icem = models.OneToOneField(
        Icem,
        on_delete=models.CASCADE,
        primary_key=True)
    productiegereed = models.CharField(max_length=30,null=True,default=True)
    productieDatum = models.CharField(max_length=30,null=True,default=True)

    def __str__(self):
        return f"{self.productiegereed}"