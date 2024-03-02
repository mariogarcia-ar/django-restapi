from rest_framework import serializers
from . import models 

class ProjecSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = ('id','title', 'description', 'technology', 'created_at')
        read_only_fields = ('created_at',)