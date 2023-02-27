from rest_framework import serializers
from .models import Site


# Site Serializer

class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = '__all__'