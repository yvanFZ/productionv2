from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from phonenumber_field.modelfields import PhoneNumberField
from datetime import date
from django.contrib import admin

#role model
class Role(models.Model):

    role_name = models.TextField(max_length=10)
    
    def __str__(self):
        return f"{self.role_name}"
    

 # functie model 
class Functie(models.Model):

    functie = models.CharField(max_length=30,help_text='Enter Functie')
    rol = models.ForeignKey(Role, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.functie}"
    
#user model
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    is_loggedin = models.BooleanField(default=False)
    last_login = models.DateTimeField(default="1900-01-01T13:20:30+03:00")
    is_staff = models.BooleanField(default=False)
    functie = models.ForeignKey(Functie,null=False, on_delete=models.CASCADE)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['is_staff','functie']

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.email}"

    class Meta:
        ordering = ('date_joined',)

# medewerker model
class MedewerkerProfile(models.Model):   
    
    #add this class and the following fields
    user = models.OneToOneField(CustomUser,null=False, on_delete=models.CASCADE)
    voornaam = models.CharField(_('voornaam'),max_length=30,null=False)
    voorletter = models.CharField(max_length=1,null=True)
    tussenvoegsel = models.CharField(max_length=4,null=True)
    achternaam = models.CharField(_('achternaam'),max_length=30,null=False)
    geslacht = models.CharField(max_length=30,null=False)
    geboortdatum= models.CharField(max_length=30,null=False)
    phone_no = models.CharField(max_length=255,null=False)
    fax_number = PhoneNumberField(blank=True)
     
    def __str__(self):
        return f"{self.achternaam}"
    class Meta:
        ordering = ('voornaam','achternaam','voorletter')


# klant woningbouw
class klantWoningbouw(models.Model):
    name = models.CharField(max_length=30,null=False)
    phone_no = PhoneNumberField()
    fax_number = PhoneNumberField(blank=True)
    straat = models.CharField(max_length=30,null=False)
    postcode = models.CharField(max_length=30,null=False)
    provincie = models.CharField(max_length=30,null=False)
    land  = models.CharField(max_length=30,null=False)
    # contactperson = models.ForeignKey(KlantProfile,null=True, default=False, blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

    