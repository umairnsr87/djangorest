from rest_framework import serializers
from .models import data_for_verification

#make a class next
class data_for_verification_serializer(serializers.ModelSerializer):
    class Meta:
        model=data_for_verification
        fields='__all__'