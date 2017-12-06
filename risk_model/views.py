# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import RiskType, RiskField
from rest_framework import viewsets
from serializers import RiskTypeSerializer, RiskFieldSerializer
from django.shortcuts import render


def index(request):
    return render(request, 'risk_model/index.html')


class RiskTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows RiskType objects to be viewed or edited.
    """
    queryset = RiskType.objects.all().prefetch_related('riskfield_set')
    serializer_class = RiskTypeSerializer


class RiskFieldViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows RiskField to be viewed or edited.
    """
    queryset = RiskField.objects.all()
    serializer_class = RiskFieldSerializer
