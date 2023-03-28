from rest_framework import serializers

from enterprise.models import Enterprise

class EnterpriseSerializer(serializers.Serializer):
    class Meta:
        model= Enterprise
        fields=["name","email","phone","active"]