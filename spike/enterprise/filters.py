from django.db import models
from django_filters import rest_framework as filters

from enterprise.models import Enterprise


class EnterpriseFilter(filters.FilterSet):
    class Meta:
        model= Enterprise
        fields={
            "name",
            "active"
        }