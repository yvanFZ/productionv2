from rest_framework import serializers
from .models import  Role, CustomUser , Functie, MedewerkerProfile,klantWoningbouw

# create
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id' ,'role_name')

class FunctieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Functie
        fields = ('id' ,'functie','rol_id')

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        read_only_field = ['created', 'date_joined']

class MedewerkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedewerkerProfile
        fields = '__all__'


class klantWoningbouwSerializer(serializers.ModelSerializer):
    class Meta:
        model = klantWoningbouw
        fields = '__all__'
        


