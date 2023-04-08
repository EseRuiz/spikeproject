from enterprise.models import Enterprise
from enterprise.serializers import EnterpriseSerializer
from enterprise.filters import EnterpriseFilter
from rest_framework import viewsets
from  rest_framework.decorators import action
from rest_framework.response import Response


class EnterpriseViewSet(viewsets.ModelViewSet):
    queryset =Enterprise.objects.all()
    serializer_class= EnterpriseSerializer
    filterset_class=EnterpriseFilter
    
    @action(detail=True,methods=['PATCH','GET','PUT'])
    def set_name(self,request,pk=None):
        queryset = Enterprise.objects.all()
        serializer=self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    
