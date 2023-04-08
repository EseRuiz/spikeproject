from rest_framework import serializers

from enterprise.models import Enterprise

class EnterpriseSerializer(serializers.ModelSerializer):
    class Meta:
        model= Enterprise
        fields=["id","name","email","phone","active"]
        
    def validate_name(self,value):
        if len(value)<4:
            raise serializers.ValidationError("falla de nombre, nombre muy corto")
        return value