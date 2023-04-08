from enterprise.models import Enterprise
from enterprise.serializers import EnterpriseSerializer
from rest_framework import viewsets



class EnterpriseViewSet(viewsets.ModelViewSet):
    queryset =Enterprise.objects.all()
    serializer_class= EnterpriseSerializer
    

    
