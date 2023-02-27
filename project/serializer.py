from csv import field_size_limit
from dataclasses import fields
from rest_framework import serializers
from .models import Project, ProjectIcem, KlantMedewerker,Klant



# Klant Serializer

class KlantMedewerkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = KlantMedewerker
        fields = '__all__'


# Klant Serializer

class KlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klant
        fields = '__all__'

# Project Serializer

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

# project icem Serializer

class ProjectIcemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectIcem
        fields =  '__all__'