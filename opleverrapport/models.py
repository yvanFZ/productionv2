from django.db import models
from testrapport.models import Testrapport
from mpo.models import Site 
from users.models import MedewerkerProfile
from project.models import Project 

# Create your models here.
class Opleverrapport(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    last_edit_datum = models.CharField(max_length=30,null=True,default='')
    author = models.ForeignKey(MedewerkerProfile, on_delete=models.CASCADE)
    # binnendel velden
    druktest = models.BooleanField(default=0)
    vacumeren = models.BooleanField(default=0)
    datatest_npi_tool = models.BooleanField(default=0)
    pragrammeren_warmtepomp = models.BooleanField(default=0)
    testHomecontroller = models.BooleanField(default=0)
    doorvoeren_afgedicht = models.BooleanField(default=0)
    leiding_afgedopt = models.BooleanField(default=0)
    reinigen_module = models.BooleanField(default=0)
    visuele_inspectie_binnenzijde = models.BooleanField(default=0)
    visuele_inspectie_buitenzijde = models.BooleanField(default=0)
    bouwrouting_op_unit = models.BooleanField(default=0)
    transportklarr_gemaakt = models.BooleanField(default=0)
    # missende onderdelen
    router = models.BooleanField(default=0)
    poe24v = models.BooleanField(default=0)
    poe48v = models.BooleanField(default=0)
    din_rail = models.BooleanField(default=0)
    utp_kabel_groen = models.BooleanField(default=0)
    utp_kabel_blauw = models.BooleanField(default=0)
    utp_kabel_grijs = models.BooleanField(default=0)
    utp_kabel_zwart = models.BooleanField(default=0)
    boilersensor = models.BooleanField(default=0)
    th1_kabel_display_kabel = models.BooleanField(default=0)
    homeController_set = models.BooleanField(default=0)
    omvormer = models.BooleanField(default=0)
    sem_kast = models.BooleanField(default=0)
    kwh_meter = models.BooleanField(default=0)
    p5stekker_omvormer = models.BooleanField(default=0)
    kampstrup_meter_21 = models.BooleanField(default=0)
    landis_gyr_meter = models.BooleanField(default=0)
    wtw = models.BooleanField(default=0)
    soft_encloser = models.BooleanField(default=0)
    tongdy = models.BooleanField(default=0)
    procon = models.BooleanField(default=0)
    antenne = models.BooleanField(default=0)
    afvoer_flexbuis_slang = models.BooleanField(default=0)
    sifon = models.BooleanField(default=0)
    rode_sensor = models.BooleanField(default=0)
    grijs_zwart_sensor = models.BooleanField(default=0)
    aansluitslang_zwart = models.BooleanField(default=0)
    lange_schroeven = models.BooleanField(default=0)
    vilblokjes_oranje = models.BooleanField(default=0)
    flow_sensor = models.BooleanField(default=0)
    doorlock = models.BooleanField(default=0)
    plexiplaat_e_module = models.BooleanField(default=0)
    wielen = models.BooleanField(default=0)
    opleverrapport_definitief = models.BooleanField(default=0)
    opleverrapport_definitief_datum = models.CharField(max_length=30,null=True,default='')


